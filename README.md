# gcode-ufp-thumbnails

Add Nautilus thumbnails for gcode and UFP files

Instalation
-----------

```bash
git clone https://github.com/WolfangT/gcode-ufp-thumbnails
cd gcode-ufp-thumbnails
sudo ./install.sh
```

Recomendations
--------------

This scripts alone only creates thumbnails if they are included inside the files when sliced with Cura Slicer using the create thumbnail post-procesing script.

In order to generate thumbnails for other gcode files also install [https://github.com/Spiritdude/Nautilus_Thumbnailer_GCode](https://github.com/Spiritdude/Nautilus_Thumbnailer_GCode),
but make sure to use install.sh again, in orther to rewrite the thumbnailer file.

Also check out:

 - https://srlm.io/2015/12/15/scad-thumbnailer/ for SCAD files
 
 - https://github.com/unlimitedbacon/stl-thumb for STL files
 
 - https://forum.freecadweb.org/viewtopic.php?t=48509 for FreeCad files

But be sure to replace:

    Exec=stl-thumb -s %s %i %o

to

    Exec=/usr/bin/xvfb-run -a -s "-screen 0 1400x900x24 -ac +extension GLX +render -noreset" stl-thumb -s %s %i %o
 
 and 
 
    Exec=/home/user/bin/scad-thumbnailer.sh %i %o %s
 
 to

    Exec=/usr/bin/xvfb-run -a -s "-screen 0 1400x900x24 -ac +extension GLX +render -noreset" openscad --autocenter --projection o --export-format png --imgsize=%s,%s -o %o %i

When using GNOME and nautilus, as it uses a sandbox that blocks X11 access

Also https://askubuntu.com/questions/1368910/how-to-create-custom-thumbnailers-for-nautilus-nemo-and-caja provides a great documentation for creating you own thumbnails
