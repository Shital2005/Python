def binary_search(arr,low,high,target):
    while low<=high:
        mid = int(low+(high-low)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            low = mid+1
        else:
            high = mid-1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
target = 10
print(binary_search(arr,0,len(arr)-1,target)) # 9





