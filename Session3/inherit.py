class College:
    def collegename(self):
        print ("ABC College")

class Student(College):
           def student_info(self):
               print ("Arjun")
               print ("101")
obj = Student()
obj.College_name()
obj.student_info()