# Inner function :
#     When we write a function inside one function is called as inner function.
#     Inner function is use when we need to combine all the small function into one.
#     Or if we want to access a parameter / varibale of the parent function.
#     When we access a parameter / varibale is called as clouser.
#     We don't need to use inner function when one of the function is use at 
#         multiple places.

#     Syntax :
#         def main_function():
#             def sub_function1():
#                 statement

#             def sub_function2():
#                 statement
#     Example :

def parent_function():
    print("Parent function")

    def child_function():
        print("This is my child function")

    child_function()

parent_function()

# Call function outside of the main function.
def parent1():
    print("This is parent 1")

    def child1():
        print("This is child 1")

    return child1
w = parent1() # "This is parent 1" , return value = child1
w() # child1()

# Clouser :
def parent(name):
    print("This is my parent function")
    lastname = 'xyz'

    def child():
        print(f"My name is {name}")
        print(f"Last name is {lastname}")

    child()

parent("Purvi")

