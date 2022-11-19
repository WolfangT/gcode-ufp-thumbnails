#!/usr/bin/env python3

"""ufp-thumb.py
wolfang torres, wolfang.torres@gmail.com

Extract thumbnails from ufp files
"""

import sys
import os
import zipfile


IMG_LOC = "/Metadata/thumbnail.png"


def main(fin, fout, size):
    zfile = zipfile.ZipFile(fin)
    if IMG_LOC not in zfile.namelist():
        print("thumbnailer error: doenst have image")
        sys.exit(os.EX_DATAERR)
    else:
        image = zfile.read(IMG_LOC)
    with open(fout, "wb") as thumb:
        thumb.write(image)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("add args [in file] [out file] [size]")
        sys.exit(os.EX_USAGE)
    else:
        fin, fout, size = sys.argv[1:4]
    main(fin, fout, int(size))
    sys.exit(os.EX_OK)
