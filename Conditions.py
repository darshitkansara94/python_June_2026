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




