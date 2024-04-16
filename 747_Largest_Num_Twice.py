# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        # Initialize indices and values for the largest and the second largest elements
        idx, largest, second = -1, -1, -1

        # Loop through each number/index in the list
        for i, num in enumerate(nums):

            # Check if the current number is greater than the largest found so far
            if num > largest:

                # If yes, update the largest to current number, and update second largest to the previous largest
                largest, second = num, largest

                # Update the index of the largest number
                idx = i

            # If the current number isn't the largest, check if it's larger than the second largest
            elif num > second:

                # If yes, update the second largest number
                second = num
                
        # Check if the largest number is at least twice as large. If yes, return its index. If no, return -1
        return idx if largest >= 2 * second else -1
