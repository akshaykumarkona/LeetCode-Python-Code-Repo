# ## Question:


# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".
 


# Code:

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=0
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                sub_str=s[i:j]
                if len(sub_str)==3:
                    flag=0
                    for k in set(sub_str):
                        if sub_str.count(k)>1:
                            flag=1
                    if flag==0:
                        n+=1
        return n