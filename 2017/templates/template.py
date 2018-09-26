#!/usr/bin/env python3

from pwn import *

r = remote(host="xxxxx", port=xxxxx)


# Exploit here
ret = r.recvuntil("xxxxx")
print(ret)

# send the payload
data = b"xxxxx"
r.sendline(data)

r.interactive()
