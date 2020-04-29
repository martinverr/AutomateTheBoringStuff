#Selective Copy
# Write a program that walks through a folder tree and searches for files with
# a certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.

import os, shutil

ext = input("Extension: ")

if not os.path.exists(f"./selectiveCopy"):
    os.mkdir(f"./selectiveCopy")

    
for folder, subfolder, files in os.walk("."):
    for file in files:
        if file.endswith(f".{ext}".lower()):
            filename = os.path.basename(file)
            shutil.copy(file, f"./selectiveCopy/{filename}")
            print(file, "copied")
