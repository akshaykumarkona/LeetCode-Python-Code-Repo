# ## Question:

# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
 

# Constraints:

# -107 <= num <= 107



# Code:

class Solution:
    def convertToBase7(self, num: int) -> str:
        num=int(num)
        remainders=[]

        if num==0:
            return "0"

        sign = "-" if num<0 else ""
        num=abs(num)

        while num:
            remainders.append(str(num%7))
            num=num//7
        return sign + "".join(reversed(remainders))


#         Example: Converting 2181 (base 10) to base 7:
# 2181 / 7 = 311 R 4
# 311 / 7 = 44 R 3
# 44 / 7 = 6 R 2
# 6 / 7 = 0 R 6 
# Reading the remainders from bottom to top (6, 2, 3, 4), we get 6234 (base 7). 
# Now, 6234 is the base 7 representation of 2181
