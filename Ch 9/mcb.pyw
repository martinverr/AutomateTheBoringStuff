import pyperclip, shelve, sys
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw del <keyword> - Delete keyword from mcbData.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw reset - Delete all keywords in mcbData.
   
#Check command line argument
if len(sys.argv) < 2 or len(sys.argv) > 3: exit()

mcbData = shelve.open('mcbData')
#If argument is "save"
if sys.argv[1] == 'save' and len(sys.argv)==3:
    mcbData[sys.argv[2]] = pyperclip.paste()

elif sys.argv[1] == 'del' and len(sys.argv)==3:
    del mcbData[sys.argv[2]]

#If argument is "list"
elif sys.argv[1] == 'list' and len(sys.argv)==2:
    pyperclip.copy(str(list(mcbData.keys())))

#If reset
elif sys.argv[1]=="reset" and len(sys.argv)==2:
    for i in list(mcbData.keys()):
        del mcbData[i]

#Else
else:
    try:
        pyperclip.copy(mcbData[sys.argv[1]])
    except KeyError:
        print("Key Not Found in mcbData")
mcbData.close()

exit()
