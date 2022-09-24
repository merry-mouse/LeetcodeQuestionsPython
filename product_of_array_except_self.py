""" 238. Product of Array Except Self
TASK: Given an integer array nums, return an array answer such that answer[i] is equal to the product
 of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
# SOLUTION
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ we are going to create 2 lists
        in each list we store 1
        then we store there product of our 'chain' calsculations"""
        countChain = [1] # in countChain numbers will be stored in order
        reverseCountChain = [1] # in reverseCountChain numbers will be  stored in reverse order
        for i in range(len(nums)-1):
            """multiply the first number of the countChain list with the first number in nums
            store this number next after number 1
            repeat it with the next number so we get [1,1,2,6]
            1*1 = 1 [1,1]; 1*2 = 2 [1,1,2]; 2*3=6 [1,1,2,6]"""
            x = countChain[i]*nums[i] 
            countChain.append(x)
        for i in range(1,len(nums)):
            """multiply the last number in reverseCountChain list with the last number in nums
            store this number first before number 1
            repeat it with the next number so we get [24,12,4,1]
            1*4 = 4 [4,1]; 4*3 = 12 [12,4,1]; 12*2=24 [24,12,4,1]"""
            x = reverseCountChain[-i]*nums[-i]
            reverseCountChain.insert(0, x)
        return [item1 * item2 for item1, item2 in zip(countChain, reverseCountChain)] # multiply lists

