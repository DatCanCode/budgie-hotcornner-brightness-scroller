# Brightness And Volume Scroller

A plugin for [Budgie HotCornersII](https://github.com/UbuntuBudgie/budgie-extras/tree/master/budgie-hotcorners) to change screen brightness or volume.

---

![Screenshot](data/config.gif)

## Features

- Changes screen brightness by scrolling mouse wheel.
- Changes volume by scrolling mouse wheel.
- Auto-closes when mouse leaves a corner.
- Uses `xdotool` to send function keys.

## Install

- I'm not a professional linux developer. I made this and it works on my Ubuntu Budgie 18.04 Bionic.
- Download or clone this repository.
- Find your mouse event file by running:
-     sudo cat /proc/bus/input/devices
- Change `mouseEvent` to your path of mouse event.
- Add this script path to [Budgie HotCornersII](https://github.com/UbuntuBudgie/budgie-extras/tree/master/budgie-hotcorners)


## References

[Ubuntu Budgie](https://ubuntubudgie.org/)<br>
[XF86 keyboard symbols](http://wiki.linuxquestions.org/wiki/XF86_keyboard_symbols) <br>
[xdotool](http://manpages.ubuntu.com/manpages/bionic/man1/xdotool.1.html)


## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or at your option) any later version.