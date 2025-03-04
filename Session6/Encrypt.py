#input: abcdefghij klmnopqrstuv
#output:j

input = "abcdefghij klmnopqrstuv"
for i in range(len(input)):
    if input[i] == " ":
      print(input[i-1])


      