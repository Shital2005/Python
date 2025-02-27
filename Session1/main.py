#READING A FILE

# f = open ('myfile.txt', 'r')
# print (f.read())
# f.close

#WRITING TO A FILE

# f = open ('myfile.txt', 'w')
# f.write('Hello World')
# f.close

#APPENDING TO A FILE

# f = open ('myfile.txt', 'a')
# f.write('Hello World')
# f.close

#Another way to append a file

# with open('myfile.txt', 'a') as f:
#     f.write('Hi Om')

import csv

# with open('myfile.txt', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open('new_myfile.txt', 'w') as new_file:
#     writer= csv.writer(new_file)

#     for line in reader:
#         writer.writerow(line)

mydict = [{'Passenger':'1','Id':'0','Survived':'1'},
          {'Passenger':'2','Id':'1','Survived':'1'},
         {'Passenger':'3','Id':'1','Survived':'3'}]

fields = ['Passenger','Id','Survived']
filename = 'new_myfile.txt'

with open( 'new_myfile.txt', 'w') as new_csv_file:
    writer = csv.DictWriter(new_csv_file, fieldnames=fields,delimiter=':')
    writer.writeheader()
    writer.writerows(mydict)    
