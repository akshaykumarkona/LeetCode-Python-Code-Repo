# ## Question:

# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

# Example 1:


# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# Example 2:


# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
 


# Code:

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indices_1=[ind for ind, val in enumerate(nums) if val==1]
        for ind in range(len(indices_1)-1):
                if indices_1[ind+1]-indices_1[ind]<=k:
                    return False
        return True
