# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/ 

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(

            # Calculate the difference between consecutive days prices
            curr - prev for prev, curr in zip(prices, prices[1:]) 

            # Include only positive differences, indicating profit
            if curr - prev > 0
        )
