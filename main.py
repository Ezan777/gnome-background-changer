import os
import random

PATH_TO_WALLPAPERS = "YOUR PATH GOES HERE"

wallpapers = os.listdir(PATH_TO_WALLPAPERS)

random_index = random.randrange(len(wallpapers))
random_wallpaper = wallpapers[random_index]

# Set the random wallpaper for light mode
os.system("gsettings set org.gnome.desktop.background picture-uri " + PATH_TO_WALLPAPERS + random_wallpaper)
# Set the random wallpaper for dark mode
os.system("gsettings set org.gnome.desktop.background picture-uri-dark " + PATH_TO_WALLPAPERS + random_wallpaper)