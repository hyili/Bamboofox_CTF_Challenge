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
    p = subprocess.Popen([script, pub_key, secret_msg, str(i+1)], stdout=subprocess.PIPE)
    out, err = p.communicate(timeout=36)
    print(err)
    p.wait()
    
    ans = out.split(b"\n")
    print(ans)
    
    # send the payload
    print(" [*] Sending payload")
    data = ans[0]
    r.sendline(data)
    
    temp1 = int(ans[1].decode())
    temp2 = int(ans[2].decode())
    p, q = (ans[1], ans[2]) if temp1 > temp2 else (ans[2], ans[1])
    
    data = p
    r.sendline(data)
    
    data = q
    r.sendline(data)

r.interactive()
