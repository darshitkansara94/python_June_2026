# Sets :
#     Set is a datatype like tuple, dictionary and List.
#     This is unordered type of data. That means in o/p sequence of the values might be changed
#         during the execution.
#     We can not modify the existing set type but we can remove and access 
#         the value from sets type.

#     Syntax :
#         variable_name = {value1,value2,value3,...,valueN}

#     Example :
sets = {10,20,50,5,25}
print(sets)

# val1 = sets[0]
# print(val1)

#remove :
#   Remove method will throw error if the value is not found

#   Example :
# sets.remove(2)

# Discard :
#    Discard method will not raise an error if value is not found

#   Example :
sets.discard(10)
print(sets)

sets.add(26)
print(sets)