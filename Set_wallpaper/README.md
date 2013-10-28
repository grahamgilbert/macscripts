# set_desktops.py

## Overview

This script will set all desktops for the current user to the specified image. This is designed to be run using a LaunchAgent at first login (for example, via [scriptRunner](https://github.com/natewalck/Scripts/blob/master/scriptRunner.py)).

## Options

The following option can be passed to the script:

* ``--path`` - The path of your chosen image file

## Example

``` bash
python set_desktops.py --path /Users/Shared/Wallpapers/my_wallpaper.png
```