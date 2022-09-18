"""217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.
"""
"""Example 1:

Input: nums = [1,2,3,1]
Output: true"""

"""Example 2:

Input: nums = [1,2,3,4]
Output: false
"""
# SOLUTION 1, sort the list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 1):
            if sortedNums[i] == sortedNums[i+1]:
                return True
        return False

# SOLUTION 2, use set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set() # use set because it stores only unique values
        for i in nums:
            if i in unique:
                return True
            unique.add(i)
        return False
