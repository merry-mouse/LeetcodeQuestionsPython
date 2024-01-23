"""
645. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""


class Solution(object):
    def findErrorNums(self, nums):
        duplicate, missing = -1, -1
        for num in range(1, len(nums) + 1):
            count = nums.count(num)
            if count == 2:
                duplicate = num
            elif count == 0:
                missing = num
        return [duplicate, missing]
