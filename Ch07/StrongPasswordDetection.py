#Strong Password Detection

# note: use regex
# lenght>=8;    uppercase>=1 and lowercase>=1;    digits>=1

import re

upperCaseRegex = re.compile("[A-Z]")
lowerCaseRegex = re.compile("[a-z]")
digitsRegex = re.compile("[0-9]")

def isStrongPw(password):
    if(len(password)<8):
        return False
    if(upperCaseRegex.search(password)==None):
        return False
    if(lowerCaseRegex.search(password)==None):
        return False
    if(digitsRegex.search(password)==None):
        return False
    return True
