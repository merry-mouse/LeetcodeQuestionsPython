"""
121. Best Time to Buy and Sell Stock

Descripton:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

"""Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

"""Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

"""Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104"""

# SOLUTION 1, long and cumbersome because of 2 for loops
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0 # largest difference
        for i in range(1,len(prices)): # range 1 to (list length -1) so we can start chounting from the back of the list
            for j in range(i,len(prices)+1): # al the numbers before that until the full length of the list
                if prices[-i] - prices[-j] > maxDiff: # check the difference
                    maxDiff = prices[-i] - prices[-j] #overwrite if difference is bigger than 0
        return maxDiff

# SOLUTION 2, better, but not perfect
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNum = prices[0]
        maxDiff = 0
        for i in range(len(prices)):
            if (prices[i] < minNum):
                minNum = prices[i]
            elif (prices[i] - minNum > maxDiff):
                maxDiff = prices[i] - minNum
        return maxDiff

# SOLUTION 3 fastest solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer = 0 # we buy here
        rightPointer = 1 # we sell here
        maxProfit = 0 # maximum profit
        while rightPointer < len(prices): # create while loop to iterate through the list indexes
            if prices[leftPointer] < prices[rightPointer]: # we are only interested when lef number is smaller than right one
                currentProfit = prices[rightPointer] - prices[leftPointer] # profit at this transaction
                maxProfit = max(maxProfit, currentProfit) # update maxProfit
            else: # if not the case, we continue moving and increment ponters
                leftPointer = rightPointer
            rightPointer += 1
        return maxProfit
