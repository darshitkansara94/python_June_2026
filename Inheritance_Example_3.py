class class_A():
    def __init__(self,y): # y = 4
        self.x = y # self.x = 4
        print(self.x)

    def fn_ClassA(self,className):
        print(f"This is Class {className}")

    def fn_common(self):
        print("This is function of class A")

class class_B(class_A):
    def __init__(self,x):
        super().__init__(x)

    def fn_ClassB(self,className_B,value_of_x): # def fn_ClassB(self,'A')
        self.fn_ClassA(className_B) # Calling function of class_A , elf.fn_ClassA('A')
        print("This is class B")

    def fn_common(self):
            super().fn_common()
            print("This is function of class B")

    def call_aprentClass_Method(self):
         super().fn_common()

obj_class_b = class_B('4') # Create an object for child class "Class_B"
# When i create object for child class (Class_B) i can access all the methods and 
#   property of my parent class (Class_A).

obj_class_b.fn_ClassB('A','3') # Calling function of class_B
# obj_class_b.fn_ClassA() # Calling function of class_A

# obj_class_b.fn_common() # Calling a method of child class

obj_class_b.call_aprentClass_Method() # Calling a method of parent class through child class