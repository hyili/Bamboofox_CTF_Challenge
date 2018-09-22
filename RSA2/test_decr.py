#!/usr/bin/env python3

import subprocess
from pwn import *

r = remote(host="bamboofox.cs.nctu.edu.tw", port=11200)
script = "./decr.sh"

for i in range(1, 33, 1):
    ret = r.recvuntil("secrect msg :", drop=True, timeout=1)

    msg = ""
    pub_key = ""

    with open("../tool/Temp/msg-{0}".format(i)) as f:
        msg = f.read()

    with open("../tool/Temp/pub-{0}.pem".format(i)) as f:
        pub_key = f.read().split("\n")[1]

    out = subprocess.check_output([script, pub_key, msg, str(i)])
    print(out.decode())

r.interactive()
