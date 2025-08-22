# ## Question:

# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

 

# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.


# Code:

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        dividing_index=(n//2)
        a=s[:dividing_index]
        b=s[dividing_index:]

        vowels="aeiouAEIOU"

        c1,c2=0,0
        for i in a:
            if i in vowels:
                c1+=1
        for j in b:
            if j in vowels:
                c2+=1
        if c1==c2:
            return True
        else:
            return False