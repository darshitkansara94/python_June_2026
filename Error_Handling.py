# Exception Handling:
#   Exception handling is use tohandle runtime errors.
#   When our program is in running state then possibly due to some network issue or some other reasons
#       program got failed so to display custom message to the user we can use exception handling.
#   We have two block here which use to handle erros. Which are try ,except and finally.
#   Try block contains actual logic or our program / code.
#   If we have any error in try block then only except block get execute. If we don't have any error
#       in try block then except is not execute.
#   Finally block, if we have error in code or not finally block always get executed in both scenerio.
#       This block is optional. 
#   If we use try then except block is mandatory. 

#   Syntax :
        # try:
        #     Python statement
        # except :
        #     Error handling
        # finally:
        #     python statement

# Example :
value1 = 10
value2 = 20

# Without error
try:
    value3 = value1 + value2
    print(value3)
except:
    print("Addition is not possible")
finally:
    print("finally block execute")

# with error
val1 = 10
val2 = 20
# val4 = val1 + val2
try:
    val3 = val1 + val2 + val4
    print(val3)
except TypeError:
    print("Type is mismatch")
except NameError:
    print("Variable is not defined")
except:
    print("Addition is not possible")
finally:
    print("finally block execute")

# Handle list
list = ["Apple","Banana","Mango","Kiwi"]
try:
    list_4 = list[4]
except IndexError:
    print("Index is not found")

# Handle list with function
def findIndex():
    try:
        index_4 = list[4]
    except:
        print("Index is not found inside function")

findIndex()