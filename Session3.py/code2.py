class NewClass:
    def __init__(self):
        print("my name is constructor and i will always execute first")
    def show(self):
        print("welcome to class level proogramming")    

obj = NewClass()
print(obj)
obj.show()
obj2 = NewClass()        