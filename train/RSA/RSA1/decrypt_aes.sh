#!/bin/sh

for i in $(cat algo); do
    echo "============================================================================="
    echo "current algo: $i"
    echo "openssl enc -d $i -in flag.jpg.aes.enc -out out/flag_$i.jpg -pass file:aeskey;"
    openssl enc -d $i -in flag.jpg.aes.enc -out out/flag_$i.jpg -pass file:aeskey;
    echo "============================================================================="
done
