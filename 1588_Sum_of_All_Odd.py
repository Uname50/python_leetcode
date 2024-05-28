# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        # Length of the array
        n, total = len(arr), 0
        
        # Iterate over each element in the array
        for i, num in enumerate(arr):

            # Calculate the contribution of the current element to the sum of subarrays
            total += ((i + 1) * (n - i) + 1) // 2 * num
        
        # Return the sum 
        return total
