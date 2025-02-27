#input = [3,3,4,2,4,4,2,4,4]
#output = 4
#moore voting algorithm

arr = {3,3,4,2,4,4,2,4,4}
n = len(arr)
majorityElement = 0
count = 0
for i in range(n):
    