# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701



## Code: 

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        import string
        mapping={}
        all_alphabets=string.ascii_uppercase
        for i in range(26):
            mapping[all_alphabets[i]]=i+1
        
        ct=columnTitle
        ans=0
        for char in ct:
            ans=ans*26+mapping[char]
        return ans

