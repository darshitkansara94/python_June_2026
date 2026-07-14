# Operators :
#     Operators are use to perform operation on values or on variable.
#     It can be a mathemetical or assign some values.

#     Types of Operators :
#         Arithmetic Operators :
#             Arithmetic operator is use to perform calculate some values.

#             Types of Arithmetic operator :
#                 Addition (+) 
#                     Give addition of two or more than two numbers.

#                     Example :
print(2 + 2) 
value1 = 2
value2 = 5   
addition =value1 + value2
print(addition)  

        #         Substraction (-)
        #            Substraction of two values

                    # Example :
print("Substraction Example")
print( 4 - 2) 
substraction =value1 - value2
print(substraction)  

        #         Division (/)
        #           Division of two numbers

                    # Example :
print("Division Example")
print(4 / 2)           
value3 = 10
value4 = 0
# division = value3 / value4 # Throw error as can not divide value by zero
# print(division)

division  = value1 / value2
print(division)

        #         Multiplication(*) :
        #           Multiply two or more than two numbers

                    # Example :
print("Multiplication Example")
print(10 * 10)
multiply = value1 * value2
print(multiply)

        #         Modulo (%)
        #           Modulo return reminder from division

                    # Example :
print("Modulos Example")
print(10 % 2)
modulo = value1 % value2
print(modulo)

        #         Exponetial (**) :
        #           exponential is type of square root

                    # Example :
print(2 ** 2)

        #   Floor division (//)
        #       Display floor value after divide

                # Example :
print("Floor division")
print(5 // 2)

        # Assignment Operators :
            # Assignment operator use to assign the same value on the right side and calculate 
            #     numbers.

            # Types of assignment Operator :
                # Addition assignement (+=)
                    # Addition with the left side value and then assign the same value to that
                    #     variable.

                    # Example :
x = 3
x += 3 # x = x + 3 (3 + 3)
print("Addition Assignment")
print(x)

                # Substraction assignement(-=) :
                #    Substract the value and assign back to the same variable.

                    # Example :
y = 10
y -= 5 # y = y - 5 (10 - 5)
print("Substraction Assignment")
print(y)
                # Division assignement (/=) :
                #   Divide value and assign back to same variable.

                    # Example :
z  = 10
z /= 2
print(z)

                # Multiplication assignment (*=)
                #   Assign value to the same variable after multiplication done.

                    # Example :
a = 10
a *= 5
print(a)                        

        # Comparision Operators :
        #    Comparision operator use to compare two values. 

            # Types of comparision operator 
            # Equal to (==) :
            #   Compare right and left hand side value. 
            #   If both values are equal then return true else false.

                # Example :
x = 10
y = 10

print("Equal to example")
print(x == y)

            # Not equal to (!=) :
            #   Not equal to return opposite o/p of equal to.
            #   O/p is always in true or false.

                # Example :
print("Not equal to example")
print(x != y)

            # Greater than (>) :
            #   Left hand side value should be grater than right hand side. otherwise return 
            #       as false.
                # Example :
print(x > y)
a = 10
b = 20

print(b > a)

            # Greater than or equal to (>=)
            #   Left hand side value should be grater than right hand side or equal to. otherwise return 
            #       as false.
                # Example :
print(x >= y) # x > y or x == y

            # Less than (<) :
            #   Left hand side value should be less than right hand side value. Otherwise
            #       it will return false.
                # Example :
print(a < b)

            # Less than or equal to (<=) 
            #   Left hand side value should be less than right hand side value or equal to. Otherwise
            #       it will return false.

                # Example :
a = 10
b = 10
print(a <= b)

        # Logical Operators :
            # and
            # or
            # not
        # Ternary Operators :
            # Ternary operator return o/p based on condition just like if else.
            # This operator we can use when we need to display single o/p. If we have a multiple
            #     line of code  inside condition then better to use if..else.

            # Syntax :
                # variable_name = o/p if condition else o/p

            # Example :
print("Ternary Operator")
fruit = "Banana"
x = "Banana" if fruit == "banana" else "Fruit is not banana"
print(x)

# Verify days by number
day = 5
# "Mon" if day = 1
# "Tue" if day = 2
# "Wed" if day = 3
# "Thu" if day = 4
# "Fri" if day = 5
# "Sat" if day = 6
# 'Sun' if day = 7

currentday = "Monday" if day == 1 else "Tuesday" if day == 2 else "Wednesday" if day == 3 else "Thursday"
print(currentday)

        # Identity Operators :
        #   If i want to verify that my two object or variable is point to the same or not.
        #   If both are point to each other then it will return true else false.
        #   We have two operators in indentity :

x = ["Banana","Mango"]
y = ["Banana","Mango"]

            # is :
            #   if both the object point to each other then it will return true.
            
                # Example :
print(x is y)
z = x
print(z)
print(z is x)            

            # is not :
            #   is not is also similar to the is operator but it will convert a o/p from true to false
            #       or false to true.

            # Example :
print(x is not y) # True
z = x
print(z)
print(z is not x) # False

        # Membership Operators :
        #   Membership operator is use to verify if string oor object contains any sequential
        #       value or not.
        #   This operator return either true or false.
        #   Two types of operator :
            # in :
            #   If value contains then return true else return false.

            # Example :
str = "Hello World"
print("H" in str)
print("llo " in str)

fruit = ["Banana","Apple","Kiwi","Sapota"]
print("Ban" in fruit) # False
print("Apple" in fruit)

            # not in :
            #   Not in return opposite o/p of actual o/p.

            # Example :
print("H" not in str) # False

print("Ban" not in fruit) # True
print("Apple" not in fruit) # False

print(fruit[1])