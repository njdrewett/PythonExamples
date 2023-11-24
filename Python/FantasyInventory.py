#Fantasy Inventory

inventoryItems = ['rope','arrow','gold','torch','dagger']

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k + ' ' + str(v))
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory,addedItems):
    for newItem in addedItems:
        try:
            inventory[newItem] = inventory[newItem] + 1
        except KeyError as notAdded:
            inventory[newItem]= 1

addToInventory(stuff, dragonLoot)

displayInventory(stuff)
