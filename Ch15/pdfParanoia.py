"""
# THIS!!!
Using the os.walk() function from Chapter 10, write a script that will go
through every PDF in a folder (and its subfolders) and encrypt the PDFs using
a password provided on the command line. Save each encrypted PDF with an
_encrypted.pdf suffix added to the original filename. Before deleting the
original file, have the program attempt to read and decrypt the file to ensure
that it was encrypted correctly.

 Then, write a program that finds all encrypted PDFs in a folder (and its
 subfolders) and creates a decrypted copy of the PDF using a provided password.
 If the password is incorrect, the program should print a message to the user
 and continue to the next PDF.
"""

import sys
import os
import PyPDF2


def decryptable(filename, passw):
    file = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(file)
    success = True if pdfReader.decrypt(passw) else False
    file.close()
    return success


def encryptPdf(passw, pdfReader, newFilename):
    destFile = open(newFilename, "wb")
    pdfWriter = PyPDF2.PdfFileWriter()
    print("Encrypting", filename, "into", newFilename)

    # copy pdfReader in pdfWriter
    for pageNum in range(1, pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    # encrypt
    pdfWriter.encrypt(passw)
    pdfWriter.write(destFile)
    destFile.close()


def getPdfFilenames(path="."):
    filenames = list()
    for root, subfolder, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                filename = root + os.path.sep + file
                filenames.append(filename)
    return filenames


# get passw from cmdline
if len(sys.argv) != 2:
    print("Invalid call. A valid call is: python pdfParanoia.py <password>")
    sys.exit()
passw = sys.argv[1]


filenames = getPdfFilenames()

for filename in filenames:
    file = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(file)

    if pdfReader.isEncrypted:
        print(filename, "is enrypted, cannot be opened\n")
        file.close()
        continue

    newFilename = filename.replace(".pdf", "_encrypted.pdf")
    encryptPdf(passw, pdfReader, newFilename)

    if not decryptable(newFilename, passw):
        print("Not able to decrypt\n", newFilename)
    else:
        print("successfully encrypted\n")
    file.close()
