class College:
    def collegename(self):
        print ("ABC College")

class Student(College):
    def student_info(self):
        print ("Arjun")
        print ("101")

class Exam(Student):
    def subject(self):
        print("subject: Python")
        print("marks: 90")
        print("grade: A")
obj = Exam()
obj.collegename()
obj.student_info()
