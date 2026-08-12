class Calculator():
    def Addition(self,val1,val2):
        return val1 + val2

    @staticmethod
    def Multiplication(val1,val2):
        print(val1 * val2)

    @staticmethod
    def Division(a,b):
        print(a / b)

calc = Calculator() # Created object for class Calculator
add = calc.Addition(10,20)
print(add)
calc.Multiplication(20,10)

class Student():
    def __init__(self,name,age):
        self.n = name
        self.age = age

    def StudentName(self):
        print(self.n)

    def StudentAge(self):
        print(self.age)

student = Student("Tushar",20)
student.StudentName()
student.StudentAge()