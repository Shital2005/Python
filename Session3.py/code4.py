class Student:
    def __init__(self):
        self.s_name = 'Arjun'
        self.s_rollno = 101

    def getdata(self):
        self.s_mb = 9999999999
obj = Student()
obj.getdata()
obj.s_branch = 'CSE'
print(obj.__dict__)
print(obj.s_mb)
del obj.s_rollno
