# ## Question:

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true




## Code

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn=list(ransomNote); m=list(magazine)

        map_counts={}
        for i in m:
            if i in map_counts:
                map_counts[i]+=1
            else:
                map_counts[i]=1
        
        for char in rn:
            if char in map_counts.keys():
                if map_counts[char]==0:
                    ans=False
                    break
                map_counts[char]-=1
                ans=True
            else:
                ans=False
                break

        return ans