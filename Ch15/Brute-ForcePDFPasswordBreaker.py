# Brute-Force PDF Password Breaker

import PyPDF2
import os
import sys

filename = input("Insert a valid path to the pdf file")
if not os.path.exists(filename):
    print("Err: Not a valid path(filename)")
    sys.exit()

PdfFile = open(filename, "rb")
DictFile = open("dictionary.txt")  # We assume nobody changed dict.txt location
passwFound = None
count = 0
pdfReader = PyPDF2.PdfFileReader(PdfFile)

# Bruteforcing words in DictFile to decrypt pdfReader
for word in DictFile:
    word = word.strip()

    count += 1
    if count % 500 == 0:
        print(f"words checked: {count} / 44000 ({count/44000*100}%) | {word}")

    if pdfReader.decrypt(word):
        passwFound = word
        break
    elif pdfReader.decrypt(word.lower()):
        passwFound = word.lower()
        break

# result
print()
if passwFound:
    print(passwFound)
else:
    print("Password not found")
# end
DictFile.close()
PdfFile.close()
