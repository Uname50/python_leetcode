# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]):
        # iterate over all numbers
        for num in nums:
            idx = abs(num) - 1
            # mark the value as visited
            nums[idx] = -abs(nums[idx])
        # iterate over nums to find positive values afterwards
        return [i + 1 for i, num in enumerate(nums) if num > 0]