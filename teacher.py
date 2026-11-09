
class Teacher:
    def __init__(self, teacher_id, teacher_name, subject):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.subject = subject

    def display_info(self):
        print("Teacher ID:", self.teacher_id)
        print("Teacher Name:", self.teacher_name)
        print("Subject:", self.subject)
        print("----------------------")


# Creating teacher objects
teacher1 = Teacher(101, "Ahmad", "Python")
teacher2 = Teacher(102, "Sharma", "Mathematics")
teacher3 = Teacher(103, "Fatima", "Computer Science")


# Displaying teacher details
print("TEACHER INFORMATION")
print("======================")

teacher1.display_info()
teacher2.display_info()
teacher3.display_info()
