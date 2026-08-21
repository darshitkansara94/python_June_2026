# Raise :
#     Raise use to error.
#     This error should be raise when user needs to put some validation and based on
#         that if we need to display some error.
#     This error is work on some codition based which is always raise when condition is 
#         not meet.
#     When we check some functionality in suring development we can use raise.

#     Syntax :
#         raise("error message")
age = -2

if age < 0: 
    raise(Exception("Age can not be less than 0"))

print("Execution completed")

# Assert :
    # Assert is also use to raise an error.
    # This exception mostly used when we publish application to the production / live.

    # Syntax :
    #     assert condition,Error_Message

    # Example :

min_age = 17

assert min_age > 18 , "Minimum age is 18"
print("Execution is completed")