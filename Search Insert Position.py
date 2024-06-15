"""

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


"""


def search_position(nums, target):

    for i in range(len(nums)):

        if nums[i] == target:

            return nums.index(target)
        
        elif nums[i] < target and nums[i+1] > target:

            return nums.index(nums[i+1])
        
        elif target > nums[-1] :

            return len(nums)

    

    


nums = [1,3,5,6]

target = 7


print(search_position(nums, target))


