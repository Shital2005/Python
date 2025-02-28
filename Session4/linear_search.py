def linear_search(input_list, target):
    for index,value in enumerate(input_list):
      if value == target:
            return index
  
    return -1
      
input_list = [1,2,3,4,5,6,7,8,9,10]
element = 10
print(linear_search(input_list, element)) # 4  
       