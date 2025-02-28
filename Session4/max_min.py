def max(input_list):
    max_num = input_list[0]
    for i in input_list:
        if i > max_num:
            max_num = i
    return max_num

def min(input_list):
    min_num = input_list[0]
    for i in input_list:
        if i < min_num:
            min_num = i
    return min_num

input_list = [1,2,3,4,5,6,7,8,9,10]
print(max(input_list)) # 10
print(min(input_list)) # 1
