# https://leetcode.com/problems/maximum-subarray/description/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to track the maximum subarray sum ending at the current position and the maximum subarray sum found so far 
        max_ending_here, max_so_far = float('-inf'), float('-inf')

        # Iterate through the input list
        for num in nums:
            # Update max_ending_here to be the maximum of the current number and the sum of the current number and the previous max_ending_here 
            max_ending_here = max(num, max_ending_here + num)
            
            # Update max_so_far to be the maximum value between the current max_so_far and the new max_ending_here
            max_so_far = max(max_so_far, max_ending_here)

        # Return the maximum subarray sum found
        return max_so_far
