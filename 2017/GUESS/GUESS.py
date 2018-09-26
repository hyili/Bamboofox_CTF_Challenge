#!/usr/bin/env python3

from pwn import *

r = remote(host="bamboofox.cs.nctu.edu.tw", port=22005)


# Exploit here
ret = r.recvuntil(b"Guess The Secret(")
ret = r.recvuntil(b" ~ ")
begin = int(ret.split(b" ")[0])
print(b"Begin: %d" % begin)

ret = r.recvuntil(b")")
end = int(ret.split(b")")[0])
print(b"End: %d" % end)

while True:
    ret = r.recvuntil(b"Input number = ")

    # send the payload
    current = (begin + end) / 2
    print(b"From: %d To: %d Current: %d" % (begin, end, current))
    data = b"%d" % (current)
    r.sendline(data)

    try:
        ret = r.recvuntil(b"Too ")
        ret = r.recvuntil(b"\n")
        result = ret.split(b"\n")[0]
        print("Result: %s" % result)

        if result == b"small":
            begin = current
        elif result == b"big":
            end = current
        else:
            break
    except Exception as e:
        print(e)
        print(ret)
        break


r.interactive()
