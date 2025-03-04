# f=open("test.txt","w")
# print("name of file",f.name)
# print("File mode",f.mode)
# print("readable",f.readable())
# print("Writeable",f.writable())
# print("File is close",f.closed)
# f.close()
# print("File is close",f.closed)

#WRITE OPERATION-Overwrites previous data

# f=open("test.txt","w")
# f.write("\n Dubai is a smart city")
# f.close()
# print("File operation is done")


#APPEND OPERATION - DOES NOT OVERWRITE PREVIOIUS Data

# f=open("test.txt","a")
# f.write("\n Dubai is a smart city")
# f.close()
# print("File operation is done")

#Append a list

# f=open("covid.txt","a")
# my_list=["apple ","mango ","cherry "]
# names={"sharmeen":"khan","Shri":"mane","mandar":"mawale"}
# tup=('hey','there')
# f.writelines(my_list)
# f.writelines(names)
# f.writelines(tup)
# print("List is inserted")
# f.close()

# READING DATA FROM FILE

# f=open("covid.txt","r")
# print(f.read())
# f.close()



#WITH STATEMENT-CLOSES THE FILE AUTOMATICALLY

# with open("test.txt","w") as f:
#     f.write("Amit\n")
#     f.write("Ashsish\n")
#     print("File is close",f.closed)
# print("File is close",f.closed)


#Image Handling

# f1=open("anki.png","rb")
# f2=open("rossom.png","wb")
# data=f1.read()
# f2.write(data)
# print("New image is available with the name: ",f2.name)


#Operation with CSV file

import csv

f=open("sudent.csv","a",newline="")
a=csv.writer(f)
a.writerow(["StudentId","ROll no","Name","Mobile No"])
num=int(input("Enter number of records: "))
for i in range(num):
    stu=int(input("Enter your id: "))
    roll=int(input("Enter your roll no: "))
    name=input("Enter your name: ")
    mobile=int(input("Enter your phone number: "))
    a.writerow([stu,roll,name,mobile])
f.close()