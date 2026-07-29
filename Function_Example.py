list = []

def printList(listValue):
    if type(listValue) == str:
        print(listValue)
    elif type(listValue) == int:
        print(listValue)
    else:
        for item in listValue:
            print(item)

while True:
    print("\nSelect Option : \n1. Insert \n2. Delete \n3. Print \n")
    userselection = int(input("Choose option : "))

    match userselection:
        case 1:
            item = input("Enter list value : ")
            list.append(item)
            print(type(item)) # str
            printList(item)
        case 2:
            itemtodelete = input("Enter item name to remove : ")
            list.remove(itemtodelete)
            printList(itemtodelete)
        case 3:
            printList(list)
        case _:
            print("Invalid choice")


# Assignment :
    # Select Type of Value
    #     1. String
    #     2. Number
