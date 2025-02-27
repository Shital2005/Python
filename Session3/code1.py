class Student:
    roll_number = 101
    num1 = 50 
    num2 = 100
    
    def add(self):
        print(self.num1+self.num2)
        self.name = input("Enter your name: ")
        print("Name is: ", self.name)

obj = Student()
obj.add()
print(obj.roll_number)