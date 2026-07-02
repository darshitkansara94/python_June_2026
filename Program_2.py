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