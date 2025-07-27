# ## Question:

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"


# Code:

class Solution:
    def reverseWords(self, s: str) -> str:
        s_splits=s.split(" ")
        new_s=[]
        for ind, i in enumerate(s_splits):
              new_s.append(i[::-1])
        return " ".join(new_s)