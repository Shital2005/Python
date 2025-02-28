class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Welcome, {self.name}")

person1 = Person('Shital')  
person1.greet()    

class Student(Person):
    def __init__(self,name,student_id):
        super().__init__(name)
        self.student_id = student_id
    @staticmethod
    def welcome(name,student_id):
        print(f"Welcome, {name} , {student_id}")

student1 = Student('Shital', 1234) 
Student.welcome("Shital", 1234)       




