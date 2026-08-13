# OOPs :
#     OOPs is a programming concept which allow developer to do
#         programming in better way and approach.
#     Full name of OOPs is Object Oriented Programming.
#     By using this concept we can create a code that is reusable and
#         readable.
#     If code is reusable than we can avoid duplication of code which give more clear 
#         undertanding of code.
#     OOPs basically have concept called class and Objects.

#     Class :
#         Class is a collection of variable and methods

#         Syntax :
#             class class_name():
#                 variables
#                 Methods / function
#     Object :
#         Object is a replication of class which allow us to access property and 
#             methods of the class.
#         We can create multiple object of the single class.

#         Syntax :
#             variable_name = class_name()


# Self :
     # Self is a keyword that indicate or point out the class itself.
     # Self keyword is a default keyword for the method if we are create that
     #      inside the class.
     # In method the first keyword is always self keyword.
     # We can create self by using any name there is no such restriction with
     #      the name of self.

# __init__ :
    __Init__ is type of constructor in python.
    This method does not return any value.
    We need to write or create constructor with the double underscore before
        keyword init and after keyword init.
    This function always has a self parameter.

    # Syntax :
        # class class_name():
        #     def __init__(self):
        #         pass


# Assignment :
    # We need to create a class with the name Student.
    # Create a constructor for the class which contain attribute / property like :
    #     Student Id,
    #     Name
    #     Age,
    #     Course,
    #     Marks
    # Create a function with the name Student_Result() where i can identify the
    #     result of the student.
    #         If marks > 35 -> Pass else Fail
    # This should be done using user input. Also we need to display a detail
    #     of the student.

# 1. Get input for StudentId,Name,Age,Course and Marks.
# 2. Need to create a class with the name Student.
#     Create constructor (__init__).
#         This constructor accpet all the values entered by user.
#             ex. __init__(self,StudentId,Name,Age,Course,Marks)
#                     self.Id = StudentId
#                     self.name = Name
#                     self.age = Age
#                     self.marks = Marks
# 3. Create a function with the name Student_Result()
#     Student_Result(self)
#         if self.marks > 35:
#             'Pass'
#         else:
#             fail
# 4. Create objet for class and pass all the input paramters.
# 5. by using object we need to call method (Student_Result())
# 6. Print Student detail
#     add function in the class with name print_student()
# 7. by using object we need to call method (print_student())


# Assignement(Date : 13 Aug) :
    # We need to create a class with the name Student.
        # Create a constructor for the class which contain attribute / property like :
        #     Student Id,
        #     Name
        #     Age,
        #     Course,
        #     Marks
        # Create a function with the name Student_Result() where i can identify the
        #     result of the student.
        #         We need to check grades. "A","B","C","D","E","F"
        # This should be done using user input. Also we need to display a detail
        #     of the student.