# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Initialize start and end to 0
        start, end = 0, 0

        # Iterate as long as the end pointer is not at the last index of the list
        while end < len(nums) - 1:

            # Update start to the current end, and end to the furthest reachable index 
            start, end = end, max(i + nums[i] for i in range(start, end + 1))

            # If the furthest reachable index does not advance, return False
            if start == end:
                return False
            
        # The end pointer has reached or surpassed the last index 
        return True
