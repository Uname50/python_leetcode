# https://leetcode.com/problems/array-partition/description/ 

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        # Sort the list in ascending order
        nums.sort()

        # Take every second element, sun the elements, return the result 
        return sum(nums[::2])
