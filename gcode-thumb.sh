#!/bin/sh

gcode-thumb.py $1 $2 $3
if [ $? != 0 ];
then
    gcode2png --autolevel --size=$3x$3 --grid=0 --dist=0.5  --rotate=30,0,-30 --output=$2 $1
fi
