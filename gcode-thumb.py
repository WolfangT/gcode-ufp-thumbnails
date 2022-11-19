#!/usr/bin/env python3

"""gcode-thumb.py
wolfang torres, wolfang.torres@gmail.com

Extract thumbnails from gcode files
"""

import os
import sys
import base64


def main(fin, fout, size):
    thumb_text = []
    reading = False
    width = None
    height = None
    img_size = None
    with open(fin, "r") as gcode:
        for line in gcode:
            if line.startswith("; thumbnail end"):
                break
            if reading:
                thumb_text.append(line.replace("; ", "", 1)[:-1])
            if line.startswith("; thumbnail begin"):
                reading = True
                width, height, img_size = list(map(int, line.split(" ")[3:6]))
                if width != size or height != size:
                    print(
                        f"thumbnail warning, image size of {width},{height}"
                        f" is not requested {size}"
                    )
        else:
            print("thumbnail error, end tag not found")
            sys.exit(os.EX_DATAERR)
    with open(fout, "wb") as image:
        data = bytes("".join(thumb_text), "utf8")
        if len(data) != img_size:
            print("thumbnail error, image size is not the stated one")
            sys.exit(os.EX_DATAERR)
        image.write(base64.b64decode(data))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("add args [in file] [out file] [size]")
        sys.exit(os.EX_USAGE)
    else:
        fin, fout, size = sys.argv[1:4]
    main(fin, fout, int(size))
    sys.exit(os.EX_OK)

