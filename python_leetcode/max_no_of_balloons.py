# #Question:

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 



# Code:


from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target="balloon"

        text_count=Counter(text)
        target_count=Counter(target)

        mini=float('inf')
        for char in target:
            current_mini=text_count[char]//target_count[char]
            mini=min(current_mini, mini)

        return mini