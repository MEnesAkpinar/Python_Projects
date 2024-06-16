"""

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


"""


def search_position(nums, target):

    for i in range(len(nums)):

        if nums[i] == target:

            return nums.index(target)
        

        elif target < nums[0]:
            
            return 0
        
        elif nums[i] > target:

            return nums.index(nums[i])
        
        elif target > nums[len(nums)-1]:

            return len(nums)

    

    


nums = [1]

target = 2


print(search_position(nums, target))



"""

def searchInsert(nums, target):

    index = - 1
    for i in range(0,len(nums)):
        if target==nums[i]:
            index = i
        
    if index==-1 and target <nums[len(nums)-1]:
        for i in range(0,len(nums)):
            if target<nums[i]:
                index = i
                break
    elif index==-1 and target > nums[len(nums)-1]:
        index = len(nums)


    return index


nums = [1,3,5,6]

target = 0


print(searchInsert(nums, target))


"""