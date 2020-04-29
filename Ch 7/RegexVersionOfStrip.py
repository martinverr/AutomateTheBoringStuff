# Regex version of strip()

import re

def strip(string, key=None):
    if key == None:
        key = ' '
    strippedRegexDx = re.compile("("+key+"*)$")
    newString = strippedRegexDx.sub("", string)
    
    strippedRegexSx = re.compile("^("+key+"*)")
    newString = strippedRegexSx.sub("", newString)

    return newString

"""
# TEST
print("xxx"+strip(" ciao   ")+"xxx")
print("xxx"+strip(" ciao   zzzzzz","z")+"xxx")
"""
