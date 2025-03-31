from collections import defaultdict

def applyOperations(nums):
    
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] * 2
            nums[i + 1] = 0
        
        non_zero_ind = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_ind] = nums[i]
            non_zero_ind += 1
    
    for i in range(non_zero_ind, len(nums)):
        nums[i] = 0
    
    print(nums)
    return nums



applyOperations(nums=[1,2,2,1,1,0])