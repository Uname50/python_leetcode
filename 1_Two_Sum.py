# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize the hash map
        hash_map = {}  
        # Iterate through the array
        for i, num in enumerate(nums):  
            # Calculate complement
            complement = target - num  
            # Check if complement exists
            if complement in hash_map:  
                # Return indices of complement and current element
                return [hash_map[complement], i]  
            # Store the element with its index
            hash_map[num] = i  