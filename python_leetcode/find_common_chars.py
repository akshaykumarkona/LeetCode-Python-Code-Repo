# ## Question:

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Code: 

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_word = list(words[0])
        for word in words[1:]:
            curr_common_chars=[]
            for char in first_word:
                if char in word:
                    curr_common_chars.append(char)
                    word=word.replace(char," ",1)
            first_word=curr_common_chars
        return first_word