class Submarks:
    math = int(input("Enter the marks of Math: "))
    DE = int(input("Enter the marks of DE: "))
    Python = int(input("Enter the marks of Python: "))
    english = int(input("Enter the marks of English: "))

class Practmarks:
    cpract = int(input("Enter the marks of C practical: "))

class Result(Submarks, Practmarks):
    def total(self):
       if self.math >= 40 and self.DE >= 40 and self.Python >= 40 and self.english >= 40 and self.cpract >= 20:
           print("Congratulations! You have passed the exam.")
       else :
           print("Fail")

    
