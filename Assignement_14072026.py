# Assignment :
    # Create a variable with the list type - var_name = []
    # User will enter the value at runtime. this value should be add into the list.
    # If user want to remove the value write a code for remove value.

# Ex : []
# z = input("Enter value :" )
# print(z)

# In this Assigment we will cover
#     List
#     input method
#     Match expression

list = []
userdecision = int(input("Enter decision : "))

match userdecision:
    case 1: # Insert
        uservalue = input("Enter value : ")
        list.append(uservalue)
        print(list)
    case 2: # Delete
        list = ["Apple","Mango","Banana"]
        deletevalue = input("Enter value to delete : ")
        list.remove(deletevalue)
        print(list)
    case _:
        print("Invalid choice")

print("Outside of match expression")