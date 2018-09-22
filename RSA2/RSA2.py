#!/usr/bin/env python3

import subprocess
from pwn import *

r = remote(host="bamboofox.cs.nctu.edu.tw", port=11200)
script = "./decr.sh"


# Exploit here
print(" [*] Reading data")

for i in range(0, 100, 1):
    ret = r.recvuntil("-----BEGIN PUBLIC KEY-----\n", drop=True)
    print(ret)
    
    ret = r.recvuntil("\n-----", drop=True)
    pub_key = ret
    print(ret)
    
    ret = r.recvuntil("secrect msg :", drop=True)
    
    ret = r.recvuntil("\n", drop=True)
    secret_msg = ret
    print(ret)
    
    # parse to decr.sh
    print(" [*] Decrypting")
    out = subprocess.check_output([script, pub_key, secret_msg, str(i+1)])
    
    ans = out.split(b"\n")
    print(ans)
    print("{0} ~ {1} ~ {2} ~ {3}".format(ans[0].decode(), ans[1].decode(), ans[2].decode(), ans[3].decode()))
    
    # send the payload
    print(" [*] Sending payload")
    data = ans[4]
    r.sendline(data)
    
    temp1 = int(ans[5].decode())
    temp2 = int(ans[6].decode())
    p, q = (ans[5], ans[6]) if temp1 > temp2 else (ans[6], ans[5])
    
    data = p
    r.sendline(data)
    
    data = q
    r.sendline(data)

r.interactive()
