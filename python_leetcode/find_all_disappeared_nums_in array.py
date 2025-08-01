# ## Question:

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]


# Code:

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set=set(nums)
        return [i for i in range(1, len(nums)+1) if i not in nums_set]
