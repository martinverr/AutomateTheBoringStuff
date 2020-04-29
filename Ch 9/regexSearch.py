from pathlib import Path
import re

#folder = "C:/Users/Martin/Desktop"
#keyRegex = re.compile(r"(\S)*@(\S)*")

folder = input("In which folder: ")
keyRegex = re.compile(input("Regex to check: "))

folderPath=Path(folder)

for checkingFile in list(folderPath.glob("*.txt")):
    f = open(checkingFile, 'r')
    if keyRegex.search(read:=f.read()) != None:
        print(keyRegex.search(read).findall())
    f.close()
