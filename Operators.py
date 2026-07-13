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
        # Ternary Operators