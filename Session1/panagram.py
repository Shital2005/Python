# str = "The quick brown fox jumps over the lazy dog"

s = input("enter string:")
s = s.lower()
s = s.replace(" ","")
a = "abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i not in s:
        print("not panagram")
        break
    else:
      print("panagram")

   
 
