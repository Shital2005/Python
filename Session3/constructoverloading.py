class Arithmetic :
    def __init__(self):
        print("Constructor")
    def __init__(self,a):
        print("Constructor with one argument")
    def __init__(self,a,b):
        print("Constructor with two arguments")
obj = Arithmetic ()
obj = Arithmetic (10)
obj = Arithmetic (10,20)        