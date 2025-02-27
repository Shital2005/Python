#common element between three arrays
a = [1, 2, 3]
b = [2, 3, 4]
c = [3, 4, 5]
for i in a :
    if i in b and i in c:
        print(i)