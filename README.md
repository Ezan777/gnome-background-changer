# Background changer

A simple script to change desktop background in gnome

## Usage

In order to work the script need a path to the wallpapers folder, you can set it in **PATH_TO_WALLPAPERS** constant.

### Launch at startup

In order to launch the script at startup the **PATH_TO_WALLPAPERS must be absolute** and you need to add this file inside `/home/$YOUR_USERNAME/.config/autostart/` you can name the file as you want but it must be a `.desktop` file with:

```
[Desktop Entry]
Encoding=UTF-8
Name=background-changer
Comment=Script that change the background
Icon=gnome-info
Exec=python3 INSERT HERE THE PATH TO THE SCRIPT
Terminal=false
Type=Application
Categories=

X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=0

```
