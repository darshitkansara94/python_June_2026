# Datatype :
#     Datatypes are present a type of data that we store inside variable memory.
#     We have a different types of datatypes like number, string, list, tules etc..
#     Datatypes helps to identify the type of data that stored in variables.

#     Types of datatype :
#      String :
#         String is a combination of alphabets, numbers and special char.
#         In python string datatype represent as "str".
#         String value always written inside single quote or double quote.

#         Syntax :
#             str(expression)

#         Example :
print("Hello World")
print(type("Hello World"))

welcomeNote = "Hello World"
print(type(welcomeNote))

number = 10 # int datatype

# Casting :
#     Convert a value from one datatype to another datatype

    # Syntax :
       # print(datatype(expression))

    # Example :
print(type(str(number)))

# Slice :
    # Slice is use to fetch char or word from string value.
    # Index always start from 0 in string.

    # Syntax :
        # variable_name[start_index:end_index]

    # Example :
string = "Hello"
        # H - 0, 
        # e - 1,
        # l - 2, 
        # l - 3, 
        # o -4

print(string[1:4])
print(string[0:])

str_Fullstring = "Hello World"
print(str_Fullstring[2:])
print(str_Fullstring[2:7])
print(str_Fullstring[:7])

# Length :
    # Length function use to identify the length or char in string.capitalize
    # Count always start with 0.

    # Syntax :
       # len(expression)

    # Example :
print(len("Hello World"))
# print(Len("Hello World")) # Display runtime error because in Len function name we 
    # have written 'L' as a capital.
