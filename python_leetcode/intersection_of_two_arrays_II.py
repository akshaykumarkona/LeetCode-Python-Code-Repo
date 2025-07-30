# ## Question:

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


# Code:
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]

        from collections import Counter

        n1=Counter(nums1)
        n2= Counter(nums2)

        dic={}

        for k,v in n1.items():
            if k in n2.keys():
                min_=min(n1[k], n2[k])
                dic[k]=min_

        for i,j in dic.items():
            for k in range(j):
                ans.append(i)

        return ans