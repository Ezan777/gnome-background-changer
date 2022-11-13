import os
import random
import functions

PATH_TO_WALLPAPERS = "YOUR PATH GOES HERE"

directories = functions.getDirectories(PATH_TO_WALLPAPERS)

images = []

for directory in directories:
    directories = directories + functions.getDirectories(directory)
    images = images + functions.getDirImages(directory)


random_index = random.randrange(len(images))
random_wallpaper = images[random_index]

# Set the random wallpaper for light mode
os.system("gsettings set org.gnome.desktop.background picture-uri " + random_wallpaper)
# Set the random wallpaper for dark mode
os.system("gsettings set org.gnome.desktop.background picture-uri-dark " + random_wallpaper)