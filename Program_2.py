# Datatype :
#     Number :
#         Number always written between 0 to 9.
#         We don't need to use double or single quote to write a numbers.

#         Types of Number :
#         int :
#             Int numbers are positive or negative.
#             Int number does not have value with the point.

#             Example :

x = 10
y = int("10")
# z = int("abc10") Execute with error

print(type(x))
print(type(y))
# print(type(z)) Execute with error

#        float :
           # Float value consider a value with the point.

            # Example :
a = int(10.50)
print(a)
print(type(a))
b = float(10)
print(b) 

# Boolean :
    # Boolean always return true or false value.
    # This value are always return from some value.

    # Example :
print(10 > 12)
print(12 > 10)

boolvalue = bool(0)

print(boolvalue)

boolexample = bool(2)
print(boolexample)

# List :
    # List is a collection of values.
    # In a list we can store a different type of data. like int or string or float etc.
    # We can use list when we need to store a multiple values in a single variable.
    # List values always written within square backets.

    # Syntax :
       # variable_name = [expression1,expression2,....,expressionN]    

    # Example :
x = "Volvo","Skoda"
carlist = ["Volvo","Skoda","Tata","BMW"]

print(x)
print(carlist)
print(type(carlist))

print(carlist[1]) # fetch value from list by using index number
print(carlist[1 : 3]) # fetch value from list by using index range
print(carlist[1:])
print(carlist[:3])

# Replace existing value in list.
     # Replace a value in the existing list on particular index.

     # Syntax :
        # list_name[index] = expression

print(carlist)
carlist[0] = "Nissan"
print(carlist)
# carlist[4] = "Volvo" - Throw "index out of range" error due to list does not contain
#    index 4.

# print(carlist[4]) - Throw "index out of range" error due to list does not contain
#    index 4.

# Modify existing list
    # To add a value in existing list.

    # 1. Insert :
        # We can insert a value at any index by using insert method

        # Example :
carlist.insert(1,"Volvo") # ["Nissan","Volvo","Skoda","Tata","BMW"]
print(carlist)

carlist.insert(5,"Toyato")
print(carlist)

    # 2. Append :
        #   Append method always add a method at the end of list.
        #   We can not add value on particular index or we do not have a 
        #   provision to add value on particular index using append.

        # Example :
carlist.append(13)
print(carlist)
carlist.append(True)
print(carlist)

print(type(carlist))

# Remove value :
    # Remove value from existing list.

    # Types of method to remove value from list
    #    1. remove :
    #       Always remove that assign into the remove method

    # Example :
print("Remove existing value from List")
print(carlist)
carlist.remove("BMW")
# carlist.remove("13") - As we have a value 13 with datatype int and we try to remove with
    # datatype string so it will not remove that value.
print(carlist)

    #    2. pop :
    #       Pop allow us to remove value from existing list.
    #       Here pop allow to remove value by using index number. And index number is
    #           optional. if user enter index number than pop will remove that value
    #           else index number is not passed then it will remove value from end
    #           of the list.

    # Example :
print(carlist)
carlist.pop() # ['Nissan', 'Volvo', 'Skoda', 'Tata', 'BMW', 'Toyato', 13]
print(carlist)
carlist.pop(2) # ['Nissan', 'Volvo', 'Tata', 'Toyato', 13]
print(carlist)

fruit = ["apple","mango","banana","apple"]
print(fruit)

fruit.remove("apple") # ["mango","banana","apple"]
print(fruit)

# Copy list :
#   To copy existing list into another variable.

# Example :
fruitlist = ["apple","mango","banana"]
print("Copy list from one to another")
fruitlistcopy  = fruitlist.copy()
print(fruitlistcopy)
print(type(fruitlistcopy))

# Sort :
#   Sort a data based on ascending order or in reverse order.
#   By default order is ascending.

# Example :
print("Sort a List")
print(fruitlist)
fruitlist.sort()
print(fruitlist)

# If we want to reverse a data then we need to use "reverse" property of sort method
fruitlist.sort(reverse = True)
print(fruitlist)

# Clear :
#   Use to clear all the values of list

# Example :
fruitlist.clear()
print(fruitlist)