class College:
    collegename = "ABC College"
    def __init__(self):
        self.studentname = 'Arjun'

principal = College()
teacher = College()
accountant = College()
print("principal = ",principal.collegename,principal.studentname)
print("teacher = ",teacher.collegename,teacher.studentname)
print("accountant = ",accountant.collegename,accountant.studentname)
College.collegename = "HBD"
principal.studentname = "Rahul"
print("principal = ",principal.collegename,principal.studentname)
print("teacher = ",teacher.collegename,teacher.studentname)
print("accountant = ",accountant.collegename,accountant.studentname)