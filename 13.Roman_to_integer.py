"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


class Solution(object):
    def romanToInt(self, s):
        # Mapping each Roman numeral symbol to a corresponding integer value
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total_sum = 0
        # iteration through all except last variables of the string
        for num in range(len(s) - 1):
            # if the value is less than the value of the next character, it indicates a subtraction
            if roman[s[num]] < roman[s[num + 1]]:
                total_sum -= roman[s[num]]
            else:
                # If current character is bigger than the next character, it adds to total_sum
                total_sum += roman[s[num]]
        # After the loop we handle the last character.It always added to total_sum
        # because there's no next character to compare it with for the subtraction rule
        return total_sum + roman[s[-1]]
