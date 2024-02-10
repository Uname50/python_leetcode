# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        
        # map Roman numerals to their integer values
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # initialize the result variable
        ans = 0
        
        # iterate over each character in the Roman numeral string
        for i in range(len(s)):
            
            # check if the current character is followed by a higher-valued character
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                
                # if true, subtract the value of the current character from the result
                ans -= values[s[i]]
            else:
                
                # otherwise, add the value of the current character to the result
                ans += values[s[i]]
        
        # return the accumulated result
        return ans
    

# solution using enumerate 
    
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0        
        dic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        for i, char in enumerate(s):
            if i+1 in range(len(s)):
                if dic[char] < dic[s[i+1]]:
                    num -= 2 * dic[char]
            num += dic[char]
        return num 
