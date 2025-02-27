name = "shital"
count = 0
ccount = 0
vow = ['a', 'e', 'i', 'o', 'u']

for i in name:
    if i in vow:
        count += 1
    else:
        ccount += 1

print(count)
print(ccount)        

