"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

import operator 
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # track the max profits
        max_ending_here, max_so_far = 0, 0 
        
        # iterate over the daily profits 
        for profit in map(operator.sub, prices[1:], prices):
            
            # update the higher value between the current max plus new profit or 0
            max_ending_here = max(max_ending_here + profit, 0)
            
            # update the overall max profit 
            max_so_far = max(max_so_far, max_ending_here)
        
        # return the max profit
        return max_so_far
