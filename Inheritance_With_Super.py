class student():
    def __init__(self,marks):
        self.mark = marks

    def students(self):
        print(f"Marks = {self.mark}")

class student_detail(student):
    def __init__(self, name, mark):        
        super().__init__(mark)
        self.name = name

    def students(self): 
        super().students() 
        print("name = " + self.name)

std_detail = student_detail("Test",15)
std_detail.students()
