#!/usr/bin/env python3

from pwn import *

r = remote(host="bamboofox.cs.nctu.edu.tw", port=22006)


# Exploit here
ret = r.recvuntil("Enter username:\n")

# send the payload
with open("shattered-1-base64.pdf", "rb") as f:
    data = f.read(-1)
    r.sendline(data)

ret = r.recvuntil("Enter password:\n")
print(ret)

# send the payload
with open("shattered-2-base64.pdf", "rb") as f:
    data = f.read(-1)
    r.sendline(data)

r.interactive()
