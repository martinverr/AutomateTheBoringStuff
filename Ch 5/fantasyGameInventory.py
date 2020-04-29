#Automatetheboringstuff Ch5: Fantasy Game Inventory

def displayInventory(inv):
    totalItems=0
    print("Inventory:")
    for nameItems in inv:
        print(inv[nameItems], nameItems)
        totalItems+=inv[nameItems]
    print("Total number of items:", totalItems)

#______________________________MAIN_____________________________________

inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)
