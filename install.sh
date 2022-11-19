#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cp gcode.xml ufp.xml /usr/share/mime/packages/
cp gcode.thumbnailer ufp.thumbnailer /usr/share/thumbnailers/
cp gcode-thumb.py gcode-thumb.sh ufp-thumb.py /usr/local/bin/


nautilus -q
rm -r ~/.cache/thumbnails/fail
update-mime-database /usr/share/mime
