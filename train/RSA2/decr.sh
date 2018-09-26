#!/bin/sh

WorkPlace="../tool/RsaCtfTool"
cd $WorkPlace

# variable
RsaCtfTool="./RsaCtfTool.py"
TempDir="../Temp"
Error="/tmp/tmp$4"

# prepare
date
echo "-----BEGIN PUBLIC KEY-----
$2
-----END PUBLIC KEY-----" > "$TempDir/pub-$4.pem"
echo "$3" > "$TempDir/msg-$4"

# crack
date
while [ 1 == 1 ]; do
## BOOMMMMMM
    $RsaCtfTool --publickey "$TempDir/pub-$4.pem" --private --attack "$1" 1> "$TempDir/priv-$4.key" 2> "$Error"
    if [ -f "$TempDir/priv-$4.key" ]; then
        result=`cat "$TempDir/priv-$4.key" | wc -l | tr -d " "`
        if [ $(($result)) -lt 4 ]; then
            >&2 printf " [-] Failed once."
            continue
        else
            break
        fi
    else
        continue
    fi
done
date
$RsaCtfTool --dumpkey --key "$TempDir/priv-$4.key" 1> "$TempDir/priv_para-$4.key"

base64 --decode "$TempDir/msg-$4" > "$TempDir/ori_msg-$4"
openssl rsautl -decrypt -inkey "$TempDir/priv-$4.key" -in "$TempDir/ori_msg-$4" -out "$TempDir/ans-$4"
date

# output
cat "$TempDir/ans-$4"
printf "\n"
cat "$TempDir/priv_para-$4.key" | awk -F' ' '/\[\*\] (p|q):/{print $3}'
