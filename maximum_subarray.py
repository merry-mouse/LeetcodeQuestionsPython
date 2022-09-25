"""53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number)
 which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23"""

# Solution 1, Brute Force, nested loops
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = set()
        if len(nums) == 1:
            return nums[0]
        maxnums = max(nums)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sums.add(sum(nums[i:j+1]))
        return max(sums) if max(sums) > maxnums else maxnums

