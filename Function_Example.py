list = [] # string
list1 = [] # Number

def printList(listValue):
    if type(listValue) == str:
        print(listValue)
    elif type(listValue) == int:
        print(listValue)
    else:
        for item in listValue:
            print(item)

def InsertValueIntoList(userValue):
    print("\nSelect Option : \n1. Insert \n2. Delete \n3. Print \n4. Exit\n")
    userselection = int(input("Choose option : "))
    match userselection:
        case 1:
            list.append(userValue) if type(userValue) == str else list1.append(userValue)             
            printList(userValue)
        case 2:
            list.remove(userValue) if type(userValue) == str else list1.remove(userValue)
            printList(userValue)        
        case _:
            print("Invalid choice")

while True:
    print("\n1. String\n2. Number\n3. Print\n4. Exit\n")
    inputType = int(input("Enter value type : "))

    match inputType:
        case 1: # string
            item = input("Enter list value : ")
            InsertValueIntoList(item)
        case 2: # number
            item = int(input("Enter list value : "))
            InsertValueIntoList(item)
        case 3:
                    print("\n1. String\n2. Number\n")
                    listType = int(input("Select Type of list : "))
                    match listType:
                        case 1:
                            printList(list)
                        case 2:
                            printList(list1)
                        case _:
                            print("Invalid choice")
        case 4:
            break
        case _:
            print("Invalid choice")




# Assignment :
    # Select Type of Value
    #     1. String
    #     2. Number
