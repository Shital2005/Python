# val1 = int(input("enter first value:"))
# val2 = int(input("enter secong number:"))
# try:
#     print(val1/val2)
# except:
#     print("can not divide")


#Two exceptions:


# try:
#     val1 = int(input("enter first value:"))
#     val2 = int(input("enter secong number:"))
#     print(val1/val2)

# except ZeroDivisionError as message:
#     print("cant divide by zero")
    
# except ValueError as message:
#     print("enter only integer")



#Multiple Exceptions in single except block 

# try:
#     val1 = int(input("enter first value:"))
#     val2 = int(input("enter secong number:"))
#     print(val1/val2)    

# except (ValueError,ZeroDivisionError) as message:
#     print(message)

# #dafault only at last 
# except:
#     print("default")   


#Else 


# try:
#     val1 = int(input("enter first value:"))
#     val2 = int(input("enter secong number:"))
#     print(val1/val2)    

# except (ValueError,ZeroDivisionError) as message:
#     print(message)

# else:
#     print("eveything is ok")    


#nested try except block 


# try:
#     val1 = int(input("enter first value:"))
#     val2 = int(input("enter secong number:"))
#     try:
#          print(val1/val2) 
#     except ZeroDivisionError as message:
#          print(message)
# except ValueError as msg:
#     print(msg)



#try,except,else,finally block



try:
    val1 = int(input("enter first value:"))
    val2 = int(input("enter secong number:"))
    print(val1/val2)

except (ValueError,ZeroDivisionError) as message:
     print(message)

else:
     print("no error")

finally:
     print("yayy")









