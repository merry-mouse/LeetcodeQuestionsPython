class Solution(object):
    def isPalindrome(self, x):
        # in a test case 0 considered as a palindrome
        if x == 0:
            return True
        # any negative number isn't a palindrome (cannot have - in the end too)
        # any number that ends with 0 isn't a palindrome, because we don't have numbers like 010
        if x < 0 or x % 10 == 0:
            return False
        x_original = x
        reversed_num = 0
        while x > 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x = x // 10
        return reversed_num == x_original
