# We need to create a reusable function.
# That function accept value from  the user and those value must be store in type of dictionary.
# I have option to add value, remove value, print dictionary.

# We need to use
#     function
#     Match expression
#     While loop
#     For loop
#     Dictionary
#     Condition

dict = {}

# dict = {
#     "name" : "John",
#     "age":"30"
# }

def addValurIntoDictionary():
    key = input("Enter dictionary key : ")
    value = input("Enter dictionary value : ")
    dict[key] = value
    print(dict)

while True:
    print("\n1. Insert\n2. Delete\n3. Print\n4. Exit\n")
    userSelection = int(input("Select option : "))

    match userSelection:
        case 1:
           addValurIntoDictionary()
        case 2:
            key = input("Enter key name to be delete : ")

            if key not in dict:
                print("Key not found in dictionary")
            else:
                del dict[key]
        case 3:
            #print(dict) # Print direct dictionary
            for key,value in dict.items():
                print(key,":",value)            
                
        case 4:
            break
        case _:
            print("Invalid choice")