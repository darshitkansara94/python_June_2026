# Special Variables :
#     Special variable is already defined into the system.
#     We can access that varibales to perform some ooperation.
#     We can not modify the variable name.
#     Special variables are accessible throgh double underscore.

print(__name__)
print(__file__)
print(__package__)

class dict():
    def __init__(self):
        self.name = "Test"
        self.lastname = "Last Name"

dit = dict()
print(dit.__dict__)