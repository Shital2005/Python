#input= [0,1,,0,3,12]
#output = [1,3,12,0,0,0]
nums = [0,1,0,3,12]
def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
print(nums)