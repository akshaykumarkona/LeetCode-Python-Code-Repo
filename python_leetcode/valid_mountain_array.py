# ## Question:

# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true


# Code:
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)

        if n<3:
            return False

        peak_index=arr.index(max(arr))

        pi=peak_index

        if pi==0 or pi==n-1:
            return False
        
        for i in range(pi):
            if arr[i]>=arr[i+1]:
                return False
        
        for j in range(pi, n-1):
            if arr[j]<=arr[j+1]:
                return False
        
        return True