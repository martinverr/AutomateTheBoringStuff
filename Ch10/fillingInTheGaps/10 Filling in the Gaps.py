## Write a program that finds all files with a given prefix, such as spam001.txt,
## spam002.txt, and so on, in a single folder and locates any gaps in the numbering
## (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the
## program rename all the later files to close this gap.
##
## As an added challenge, write another program that can insert gaps into numbered
## files so that a new file can be added.

import re, os, shutil

prefixRegex = re.compile(r"""
                        ^(.*?)      #group1 = pre_part
                        (\d\d\d)    #group2 = prefix
                        (.*?)$      #group3 = after_part
                        """, re.X)

##print("BEFORE")
##for file in os.listdir('.'):
##    
##    if prefixRegex.search(file) == None: #if not a file like 001xxxx or xx023xx and define mo(match object)
##        continue
##    print(file)

before = 0
for file in os.listdir('.'):
    
    if prefixRegex.search(file) == None: #if not a file like 001xxxx or xx023xx and define mo(match object)
        continue
    mo = prefixRegex.search(file)
    if mo.group(2) == "000":            #if the first file, skip
        continue
    if int(mo.group(2)) == before + 1:   #right, no need to correct, update "before"
        before += 1
        continue
    else:
        newname = mo.group(1) + str(before+1).rjust(3, '0') + mo.group(3)
        print(f"oldname: {os.path.basename(file)}, newname: {newname}")
        shutil.move(file, newname)
        before += 1

##print("\nAFTER")
##for file in os.listdir('.'):
##    
##    if prefixRegex.search(file) == None: #if not a file like 001xxxx or xx023xx and define mo(match object)
##        continue
##    print(file)  
