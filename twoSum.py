"""
1. Two Sum
TASK:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

"""Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. """

"""Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2] """

"""Example 3:

Input: nums = [3,3], target = 6
Output: [0,1] """

# SOLUTION
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {} # hash map (dictionary) of values and indexes
        
        for index, num in enumerate(nums): # enumerate returns a list with indexes and their values
            difference = target - num # defference between target value and value in the list
            if difference in Dict: # finding this difference in our Dict
                return [Dict[difference], index] # return answer if we have it in the Dict 
            Dict[num] = index # if not in dict, store the value and it's index
        