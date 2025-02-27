a = int(input("Enter marks of Physics: "))
b = int(input("Enter marks of Chemistry: "))
c = int(input("Enter marks of Mathematics: "))
d = int(input("Enter marks of Biology: "))
e = int(input("Enter marks of History: "))

total = a + b + c + d + e

print("Total marks: ", total)

percentage = total / 5.0

print(percentage)

if a>=40 and b>=40 and c>=40 and d>=40 and e>=40:
    print("You are passed")
else:
    print("You are failed")

if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")  
else:
    print("failed")    

     
