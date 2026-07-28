# Function :
#     Function is a block of code that performs a specific task.
#     And can be reused throughout a program. 
#     Functions help to organize code, make it more readable, and allow for modular programming. 
#     In Python, functions are defined using the `def` keyword followed by the function name and parentheses.
#     For example: If my function name is addition so we can write it as addition().
#     Function can support multiple arguments.
#     Function can also return a value by using the keyword `return`.
#     Space is not allowed in function name. 
#     Function name should not start with a number or special character.
#     To execute the function, we need to call it by its name followed by parentheses.

#     Syntax :
#         def function_name(paramaters):
#             # code block             

print("Example of function in python")

def printMessage():
    print("Hello world")

def printSecondMessage():
    print("Hello world again")

printMessage()  # Calling the function to print the message

printSecondMessage()

# Reusable Function
def printMessageWithName(personName,lastName):
    print("Hello " + personName + lastName)

printMessageWithName("Xyz","abc")

def Addition(number1,number2):
    return number1 + number2
    print("This line will not be executed because it is after the return statement")
    input("Value 1")
    input("Value 2")

addition = Addition(10,20)
print(addition)