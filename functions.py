import os

def getDirectories(path):
    directories = []
    path += "/"
    entries = os.listdir(path)

    for entry in entries:
        if os.path.isdir(path + entry):
            directories.append(path + entry)

    return directories

def getDirImages(directory_path):
    images = []
    entries = os.listdir(directory_path)

    for entry in entries:
        if not os.path.isdir(directory_path + entry):
            images.append(directory_path + "/" + entry)

    return images