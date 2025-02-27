class Hod:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.empid = rollno

    
    def show(self):
       print("My name is:",self.name)
       print("My age is:",self.age)
       print("My empid is:",self.empid)

obj= Hod('Arjun',45,101)
obj.show()