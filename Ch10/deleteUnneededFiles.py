import os

def printFileGreaterThan(path, maxSize):
    
    if not os.path.exists(path) or not os.path.isdir(path):
        return -1
    
    for folders, subfolders,filenames in os.walk(path):
        for filename in filenames:
            filename = os.path.join(folders, filename)
            if os.path.getsize(filename) > maxSize * 2 ** 20:
                print(f"\n{filename} (size: {os.path.getsize(filename)//2**20}MB)")
    return 1

#no input validation, just for test different cases
path = input("path: ")
maxSize = int(input("maxSize(MB): "))
if not printFileGreaterThan(path, maxSize):
    print("Path error")
