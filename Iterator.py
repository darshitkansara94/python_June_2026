# Iterator :
#     Iterator is a object that use to fetch value from list, tuple or string value.
#     We need to fetch all the value manually while in the loop all the values are fetched itself.
#     We need to use next statement to fecth next value.

#     Syntax :
#         varibale_name = iter(variable_name)

#         fetch next value :
#             next(variable_name)

#     Example :
list = ["Lemon","13","Mango","Banana","Apple","Orange"]

# for item in list:
#     print(item)

listIterator = iter(list)

print(next(listIterator))
print(next(listIterator))
print(next(listIterator))
print(next(listIterator))
print(next(listIterator))

string = "Hello"
print("Display string using Iteration")
stringIterator = iter(string)
print(next(stringIterator))
print(next(stringIterator))

