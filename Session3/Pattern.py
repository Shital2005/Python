# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#    for j in 




#    i = 1 
#    1,6 
#    69

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#   print(" "*(n-i), "*"*i,end=" ")
#   print()

# import time 
# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#    print(" "*(n-i),end=" ")
#    for j in range(1, i+1):
#        time.sleep(2)
#        print("*",end=" ")
#    print()


   
# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#    print(" "*(n-i),end=" ")
#    for j in range(1, i+1):
#        print(j,end=" ")
#    print()

   
n = int(input("Enter the number of rows: "))  
for i in range(1, n+1):
   print(" "*(i-1),end=" ")
   for j in range(1, n-i+2):
       print(chr(64+i),end=" ")
   print()