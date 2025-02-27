ch = ord(input("Enter a character: "))
if  ch>=65 and ch<=90:
    print("You entered an uppercase character.")
elif ch>=97 and ch<=122:
    print("You entered a lowercase character.")
elif ch>=48 and ch<=57:
    print("You entered a digit.")
else:
  print("You entered a special character.")

