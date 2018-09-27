#!/usr/bin/env python3

from pwn import *

r = remote(host="bamboofox.cs.nctu.edu.tw", port=22004)

choose_to_win = {b"!": 0, b"?": 1, b":": 2}
mapping = [b"paper", b"scissors", b"rock"]


# Exploit here
ret = r.recvuntil(b"Let's play a game")

ret = r.recvuntil(b"\n")
oppo = ret.split(b"\n")[0]
print(oppo)
choose = choose_to_win[oppo]

for i in range(0, 100, 1):
    ret = r.recvuntil(b"rock, paper, or scissors ( choose one of them ): ")
    print(ret)

    # send the payload
    data = mapping[choose]
    print(data)
    r.sendline(data)

    choose = (choose + 1) % 3

r.interactive()
