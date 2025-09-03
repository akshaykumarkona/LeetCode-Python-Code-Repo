# ## Question:

# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.



# Code:

class Solution:
    def maxPower(self, s: str) -> int:
        c,max_c=1,1

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
                max_c=max(max_c,c)
            else:
                c=1
        return max_c