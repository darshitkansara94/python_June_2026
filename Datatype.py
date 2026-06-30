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

# Concate :
    # Concatenation is merging two or more than two words and present as a single
    #     string value.

    # Example :
print("Display Concetenate example")
Fullname = "Darshit" + " " + "Kansara"
print(Fullname)

Firstname = "Darshit"
Lastname = "Kansara"
FullnameByVariable = Firstname+ " " + Lastname
print(FullnameByVariable)

fullname = "Darshit Kansara"
Age = 25
print(type(fullname))
print(type(Age))
# FullNameAndAge = fullname + Age
# print(FullNameAndAge)

# Format :
    # Merge srting and display as a single string value.
    # This function is use to display a dynamic message to the user or some 
    #   string value.
    # Format function always start with char 'f'.

    # Syntax :
        # variable_name = f"string value"

    # Example :
lastname = "Kansara"
Name = f"Darshit {lastname}"
print(Name)

AgePrint = f"Person age is : {Age}"
print(AgePrint)

FullNameWithAge = f"Person Name is {Firstname} {Lastname} and age is {Age}"
print(FullNameWithAge)
# FullnameWithAgeandplus = "Person name is " + Firstname + Lastname  + " Age is " + str(Age)

# Capitalize :
#     Capitalization use to display first char in uppercase and remain in lower case.

    # Syntax :
        # print(variable_name.capitalize())

    # Example :
helloworld = "hello WORLD"
print(helloworld.capitalize())

# Lower() :
    # Convert a string into lower case.

    # Syntax :
        # print(variable_name.lower())

    # Example :
print(helloworld.lower())

# Upper() :
    # Convert  a case into upper case

    # Syntax :
        # varibale_name.upper()

    # Example :
print(helloworld.upper())

# split :
    # split function divide a string in diff part and present in array.
    # To seperate a string we need to use seperator.
    # By default seperator is space.

    # Syntax :
        # variable_name.split()

    # Example :
print(FullnameByVariable.split())

x = "Good evening, Welcome to class"
print(x.split(","))
print(x.split())

y = "This is montain. Mountain is good"
print(y.split("is",1))