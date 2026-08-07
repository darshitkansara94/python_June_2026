# Math function :
#     Math function are use to perform mathemetical operations. 
#     Python already support some basic mathemetical operations.

#     Types of Math function :
#         min :
#           Minimum value is use to find a minimum value from the tuple.

#           Syntax :
#               min(valu1,value2,value3,...,valueN)
#           
#           Example :
x = (10,20,25,1,45)
print(min(x))
#         max :
#           Maximum value is use to find a maximum value from the tuple.

#           Syntax :
#                max(valu1,value2,value3,...,valueN)

#           Example :
print(max(x))

#         Absolute :
#           Absolute is use to convert negative value into positive value.
#           Absolute function we can use with the keyword 'abs'

#           Syntax :
#               abs(value)

#           Example :
y = abs(-7.55)
print(y)

#         Power :
#           power is exponential of the value.
#           We can use power function with the keyword 'pow'
#              
#           Syntax :
#                pow(base,exponential,[modulos])

#           Example :
z = pow(2,4)
print(z)

a = pow(2,4,2)
print(a)

# Python also provide some other mathemetical functions.
# To access those function we need to import math library.

# Types of functions :
#    1. Square root
#       Square root function return square root value.
#       We can access this fuction using math library.
#       To use this function we need to use 'sqrt' keyword.
#       
#       Syntax :
#           sqrt(value)
#       
#    2. Ceiling
#       Ceiling function use to round a value in upbound.
#       We can use this function using 'ceil' keyword.

#       Syntax :
#           ceil(value)

#    3. Floor :
#       Floor is also use to round a value but this function will round down side.
#       We can use this function using keyword 'floor'

#       Syntax :
#           floor(value)

#    4. Pi :
#       Return pi value.

#       Syntax :
#           pi

# Example :
print("Example with the math library")

import math

square_root = math.sqrt(64)
print(square_root)

ceiling = math.ceil(1.4)
print(ceiling)

floor = math.floor(1.4)
print(floor)

pi_value = math.pi
print(pi_value)