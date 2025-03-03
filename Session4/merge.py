def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    res = []
    left_pointer = right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            res.append(left[left_pointer])
            left_pointer += 1
        else:
            res.append(right[right_pointer])
            right_pointer += 1
    res.extend(left[left_pointer:])
    res.extend(right[right_pointer:])
    return res   

 