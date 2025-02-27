# class Arithmetic:
#     def add (self,a):
#         print(a)
#     def add (self,a,b):
#         print(a+b)
#     def add (self,a,b,c): 
#         print(a+b+c)
# obj = Arithmetic()
# # obj.add(10)
# # obj.add(10,20)
# obj.add(10,20,30)       


# to handle this problem 

class Arithmetic:
    def add (self,a=None,b=None,c=None):
      if a!=None and b!=None :
        print(a+b)
      elif a!=None and b!=None and c!=None:
        print(a+b+c)
      else:
        print("enter at least two args") 
obj = Arithmetic()
obj.add(10)
obj.add(10,20)
obj.add(10,20,30)    

