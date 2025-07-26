# # Question

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 


# Code:

class Solution:
    def reverseVowels(self, s: str) -> str:

        s=list(s)
        vowels="aeiouAEIOU"
        vl,il=[],[]

        for ind,i in enumerate(s):
            if i in vowels:
                vl.append(i)
                il.append(ind)


        for i,idx in enumerate(il):
            s[idx]=vl[::-1][i]
        return ''.join(s)
    