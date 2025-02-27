class Example:
     a = 10
     def __init__(self):
        Example.s_name = 'Arjun'
        self.s_rollno = 101
     def example(self):
        self.s_mb = 9999999999
        
obj = Example()
obj.example()
print(obj.s_mb)