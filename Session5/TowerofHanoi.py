# Tower of Hanoi implementation
# we can move only one disk at a time 
# pick upper disk from any one pipe and place it on top of another pipe
# we cannot place larger disk on top of smaller disk
# dont use loops, if else in code and recursion, only use oops concepts and list 
import time
class TowerOfHanoi:
    def __init__(self):
        print('Tower of Hanoi Game')
        print()
        print('Given Problem      A=[3,2,1]     B = []     C = []')
        print()
        print('Expected Outcome    A = []       B = []     C = [3,2,1]')
        self.A = []
        self.B = []
        self.C = []

    def tower (self,item):
        self.A.append(item)
        time.sleep(1)
        print("A=", self.A)
        print("Items in Tower A\n")


    def pass1(self):
        self.B.append(self.A.pop())      # B= 1    A = 3,2
        time.sleep(1)
        print("A=", self.A)
        print("B=", self.B)
        print("A =",self.A      ,"B =",self.B    ,"C =",self.C)
        print("Pass 1 Completed =========================================================================") 


    def pass2(self):
        self.C.append(self.A.pop())     #A = 3      B =1 C= 2
        time.sleep(1)
        print("A=", self.A)
        print("C=", self.C)
        print("A =",self.A      ,"B =",self.B    ,"C =",self.C)
        print("Pass 2 Completed =========================================================================")


    def pass3(self):
        self.B.append(self.C.pop())    #B =    C = 2,1  A =3
        time.sleep(1)
        print("B=", self.B)
        print("C=", self.C)
        print("A =",self.A      ,"B =",self.B    ,"C =",self.C)
        print("Pass 3 Completed =========================================================================")


    def pass4(self):
        self.C.append(self.A.pop())     #B = 1 C = 2  A = 3
        time.sleep(1)
        print("B=", self.B)
        print("A=", self.A)
        print("A =",self.A      ,"B =",self.B    ,"C =",self.C)
        print("Pass 4 Completed =========================================================================")
              

    def pass5(self):
    
        self.A.append(self.B.pop())   #A = 3,2  C =   B = 1
        time.sleep(1)
        print("C=", self.C)
        print("B=", self.B)
        print("A =",self.A      ,"B =",self.B    ,"C =",self.C)
        print("Pass 5 Completed =========================================================================")
              
    def pass6(self):
    
        self.A.append(self.B.pop())  
        time.sleep(1)
        print("A=", self.A)
        print("C=", self.C)
        print("A =",self.A      ,"B =",self.B    ,"C =",self.C)
        print("Pass 6 Completed =========================================================================")


    # def pass7(self):
    
    #     self.B.append(self.A.pop())
    #     time.sleep(3)
    #     print("A=", self.A)
    #     print("B=", self.B)
    #     print("A =",self.A      ,"B =",self.B    ,"C =",self.C)
    #     print("Pass 7 Completed =========================================================================")


obj = TowerOfHanoi()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()



              

              
              


  
    
      
    



