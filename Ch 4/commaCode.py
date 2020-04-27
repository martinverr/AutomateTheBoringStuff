#automateboringstuff ch4: Comma Code

def _isListOfStr(list_):
    for el in list_:
        if type(el) is not str:
            return False
    return True

def list2string(listArg):
    # Check if listArg is valid
    if listArg is None or len(listArg) < 1:
        return ""
    if not _isListOfStr(listArg):
        raise Exception("List contains not <str> elements")
    
    # if: listArg contains 1 element, then: return it
    if len(listArg) == 1:
        return listArg[0]

    # Concatenate listArg elements to string, except the last
    string = ', '.join(listArg[:-1])

    # Add the last item
    string = string + " and " + listArg[len(listArg)-1]

    return string

"""
# TEST

spam0 = ["apples", "bananas", "tofu", "cats"]
spam1 = []
spam2 = None
spam3 = ["Single element"]
spam4 = ["First", "second"]
spam5 = ["black", "white", 345, "green"]
spam6 = ["black", "white", "yello", "green", "apples", "bananas", "tofu", "cats"]
print("spam0:",list2string(spam0))
print("spam1:",list2string(spam1))
print("spam2:",list2string(spam2))
print("spam3:",list2string(spam3))
print("spam4:",list2string(spam4))
try:
    print("spam5:",list2string(spam5))
except Exception as err:
    print("ERR:", err)
print("spam6:",list2string(spam6))
"""
