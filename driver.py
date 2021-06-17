from mainCommands import Item, Inventory, Users, Cart
from mainCommands import items, inventoryItems, users, userCart

mapperDict = {
    "createItem": "Item",
    "addInventory": "Inventory",
    "getInventory": "Inventory",
    "search": "Inventory",
    "addUser": "Users",
    "getUserWalletAmount": "Users",
    "setUserWalletAmount": "Users",
    "addToCart": "Cart",
    "updateCart": "Cart",
    "removeFromCart": "Cart",
    "getCart": "Cart",
    "cartCheckout": "Cart"
}


def driverMapp(funcString):
    try:
        funcName = funcString.split("(")

        if len(funcName) > 0:
            funcName = funcName[0]

            if funcName in mapperDict:
                exec(mapperDict[funcString.split("(")[0]] + "." + funcString)
            else:
                print("Invalid Function!!")
        else:
            print("Invalid Function!!")
    except Exception as error:
        print("Error Occured: ", error)


if __name__ == "__main__":
    readFile = open("input.txt", "r")

    for f in readFile.readlines():
        print("*"*50)
        print(f)
        driverMapp(f)

        print(items)
        print(inventoryItems)
        print(userCart)