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

def displayMessage(): # Creation of function
    print("Display function message")

displayMessage() # Calling and executing function

print("Execute function with param")
def greeting(message, name):
    print(message , name)

value = greeting("Good morning","Darshit")

displayMessage()

greeting("Good evening","Abhishek") # calling function second time.

# Return :
    # Return statement retrun a value to the function where it start execution.
    # This is not mandatory.

def addition(num1,num2):
    return num1 + num2 #30

add = addition(10,20) # add = 30
print(add)
add1 = addition(20,40) # add1 = 60
print(add1)

print(add + add1)