class student():
    def students(self,student_marks):
        print(f"Marks = {student_marks}")

class student_detail(student):
    def students(self,name,mark):  
        super().students(mark)    
        print("name = " + name)

std_detail = student_detail()
std_detail.students("test",15)
