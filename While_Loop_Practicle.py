print("Insert a value into List")
list = [] # Empty list

while True:
    print("Please select option\n1. Insert \n2. Delete \n3. Print \n4. Exit")
    userdecision = int(input("Enter option : ")) # Get input from user for Insert, Update or Delete

    match userdecision:
        case 1:
            newvalue = input("Enter list value : ")
            list.append(newvalue)
            print(list)
        case 2:
            deletevalue = input("Enter value to delete : ")
            list.remove(deletevalue)
            print(list)
        case 3:
            i = 0
            while i < len(list):
                print(list[i])
                i += 1
        case 4:
            break
        case _:
            print("Invalid Choice")