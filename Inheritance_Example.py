# Parent class (Base class)
class class_a():
    def __init__(self,name):
        self.name = name

    def greeting(self):
        print("Good morning")

# Child class (Derived class)
class class_b(class_a): # class_b(class_a("abc"))
    def greeting1(self):
        print(self.name)
        print("Good evening")

std_detail = class_b("abc")
std_detail.greeting()
std_detail.greeting1()