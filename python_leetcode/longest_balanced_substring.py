# #Question:

# You are given a binary string s consisting only of zeroes and ones.

# A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

# Return the length of the longest balanced substring of s.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "01000111"
# Output: 6
# Explanation: The longest balanced substring is "000111", which has length 6.
# Example 2:

# Input: s = "00111"
# Output: 4
# Explanation: The longest balanced substring is "0011", which has length 4. 
# Example 3:

# Input: s = "111"
# Output: 0
# Explanation: There is no balanced substring except the empty substring, so the answer is 0.


# Code:
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n=len(s)
        all_substrings, all_valid_substrings_lens=[], []

        for i in range(n):
            for j in range(i, n):
                all_substrings.append(s[i:j+1])
        
        for sub_str in all_substrings:
            # if "0" in sub_str and "1" in sub_str:
                ll=list(sub_str)
                if sorted(ll)==ll and ll.count("0")==ll.count("1"):
                    all_valid_substrings_lens.append(len(sub_str))
            
        if all_valid_substrings_lens:
            return max(all_valid_substrings_lens)
        return 0