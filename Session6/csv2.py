import csv

f=open("student1.csv","a",newline="")
a=csv.writer(f)
a.writerow(["StudentId","Student_branch","Name","p1","p2","p3","p4","p5","Total","Percentage","grade","Result"])
num=int(input("Enter number of records: "))
for i in range(num):
    stu=int(input("Enter your id: "))
    branch=input("Enter your branch: ")
    name=input("Enter your name: ")
    p1=int(input("Enter your paper 1 marks: "))
    p2=int(input("Enter your paper 2 marks: "))
    p3=int(input("Enter your paper 3 marks: "))
    p4=int(input("Enter your paper 4 marks: "))
    p5=int(input("Enter your paper 5 marks: "))
    Total=p1+p2+p3+p4+p5
    Percentage=Total/5
    if Percentage>=90:
        grade="A"
        result="Pass"
    elif Percentage>=80:
        grade="B"
        result="Pass"
    elif Percentage>=70:
        grade="C"
        result="Pass"
    elif Percentage>=60:
        grade="D"
        result="Pass"
    elif Percentage>=50:
        grade="E"
        result="Pass"
    else:
        grade="F"
        result="Fail"
    a.writerow([stu,branch,name,p1,p2,p3,p4,p5,Total,Percentage,grade,result])
f.close()
     
   