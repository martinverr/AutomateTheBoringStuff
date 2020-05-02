#Automatetheboringstuff ch5: List to Dictionary Function for Fantasy Game Inventory

def displayInventory(inv):
    totalItems=0
    
    print("Inventory:")
    for nameItems in inv:
        print(inv[nameItems], nameItems)
        totalItems += inv[nameItems]
    print("Total number of items:", totalItems)


def addToInventory(inv, newItems):
    newInv = inv.copy()
    for item in newItems:      
        newInv.setdefault(item, 0)
        newInv[item] += 1
        #or in one line: newInv[addedItems[i]]=newInv.get(addedItems[i],0)+1
    return newInv

#________________________________MAIN_______________________________

inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inventory)
print("\n\nUpdated ", end="")
displayInventory(addToInventory(inventory, dragonLoot))
