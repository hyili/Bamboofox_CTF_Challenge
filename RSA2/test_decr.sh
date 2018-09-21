#!/bin/sh



for i in $(seq 1 20);
do
    msg=`cat ../tool/Temp/msg-$i`
    pub_key=`head -n 2 ../tool/Temp/pub-$i.pem | tail -n 1`


    ./decr.sh $pub_key $msg $i
done
