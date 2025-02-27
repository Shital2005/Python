# a = [1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# def func(value,values):
#     var = 1
#     values[0]=44
# t=3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])


# data = [[[1,2],[3,4]],[[5,6],[7,8]]]
# def fun(m):
#     v = m[0][0]
#     for row in m:
#         for element in row:
#             if v<element : v=element
#     return v
# print(fun(data[0]))        


# arr = [[1,2,3,4],
#       [4,5,6,7],
#       [8,9,10,11],
#       [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# def f(i,values= []):
#     values.append(i)
#     print(values)
# f(1)   
# f(2)
# f(3)

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]= arr[i]
# for i in range(0,6):
#     print(arr[i],end= "")   


# fruit_list1 = ['apple','berry','cherry','papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'guava'
# fruit_list3 [1] = 'kiwi'

# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'guava':
#         sum += 1
#     if ls[1] == 'kiwi':
#         sum +=20
# print(sum)


# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[1,2])
# print(a[4,5])


#keyerror
# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])


# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1

# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))


# arr ={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)


# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)  

#30

my_dict = {}
my_dict[(1,2,4)]=8
my_dict[(4,2,1)]=10
my_dict[(1,2)]=12

sum = 0
for k in my_dict:
    sum += my_dict[k]
print(sum)
print(my_dict)


