# Conditions :
#     Conditions are use to execute code based on some output.
#     This output always return true or false.
#     In condition indent is important.

    # Types of condition :
        # If else :
            # We have two block of code. 
            # If condition is true then If part is executed and if false then else code will get executed.
            
            # Syntax :
                # if condition:
                #     Python Code
                # else:
                #     python code

            # Example :
if 5 > 6:
    print("5 is greater than 6")
else:
    print("5 is less than 6")

# Condition with If statement only
if 5 < 6: 
    print("5 is less than 6")

print("Condition is not executed")

# Write condition with variables
print("Condition with variables")

value1 = 10
value2 = 20

if value1 > value2: # 10 > 20 = false
    print("10 is greater than 20")
else:
    print("10 is less than 20")

value1 = 0
value2 = 0.1

if value2 == value1:  # 0.1 > 0
    print("If condition executed")
else:
    print("else condition executed")

# if elif else :
    # This is extended version of If else condition.
    # Here we can verify multiple condition and based on that we will get a o/p.

    # Syntax :
        # if condition1:
        #     Python code
        # elif condition2:
        #     python code
        # elif condition3:
        #     python code
        # .
        # .
        # else:
        #     python code

        # Example :
car = "Tata"

if car == "tata": # Tata = tata = false
    print("Purchased tata")
elif car == "Mahindra":
    print("Purchased mahindra")
elif car == "Skoda":
    print("Purchased skoda")
else:
    print("Drop plan")
#################################################
if car == "tata".capitalize():
    print("Purchased tata")
elif car == "Mahindra":
    print("Purchased mahindra")
elif car == "Skoda":
    print("Purchased skoda")
else:
    print("Drop plan")

######################################
if car.lower() == "tata":
    print("Purchased tata")
elif car == "Mahindra":
    print("Purchased mahindra")
elif car == "Skoda":
    print("Purchased skoda")
else:
    print("Drop plan")

# Logical Operators :
# and :
#     And operator denotes all the condition must be true then only condition is satisfied.

#     Example :
#         5 > 6 and 6 > 5 = False
#         6 > 4 and 10 < 12 = True
# or :
#     If any condition is true then we will get output as a true. If all condition is false then only
#         we will get as false.

#     Example :
#         5 > 6 or 6 > 5 = True
#         5 > 6 or 10 > 12 = False

# not :
#     Not convert actual output into opposite. 
#     If we get o/p as a true then not convert it into false. And of we get o/p as false then
#         not convert into true.

#     Example :
#         5 > 6 = True
#         10 < 12 = False

# Example
if 5 > 6 and 6 > 5:
    print("if statement executed")
else:
    print("Else statement executed")

if 6 > 5 and 10 < 12:
    print("if statement executed")
else:
    print("else statement executed")

if 6 > 5 or 10 > 12:
    print("If statement executed")
else:
    print("Else statement executed")

if (6 > 5 or 10 > 12) and (10 > 12 or 5 < 6): # True and True
    print("If statement executed")
else:
    print("Else statament executed")

if (6 > 5 and 10 < 12) or (10 > 12 and 5 < 6): # True or False
    print("If statement executed")
else:
    print("Else statament executed")

if not 6 > 5:
    print("If statement execute")
else:
    print("Else statement execute")

if not (6 > 5 and 10 < 12) and not (6 > 5 and 10 > 12): # False and True = False
    print("If statement executed")
else:
    print("Else statament executed")

if not (6 < 5 and 10 < 12) and not (6 > 5 and 10 > 12): # True and True = True
    print("If statement executed")
else:
    print("Else statament executed")

# Pass :
#    Pass keyword use to write inside if or else statement if actual logic is not implemented.

    # Example :
if 5 < 6:
    pass
else:
    print("else execute") 

# Assignment :
    # Take one varible and assign mark between 0 - 100.
    # Write a code that return grade based on mark value.
    #     Condition :
    #         90 - 100 = Grade A
    #         75 - 89 = Grade B
    #         65 - 74 = Grade C
    #         55 - 64 = Grade D
    #         35 - 54 = Grade E
    #         Below 35 = Grade F





