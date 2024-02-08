# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# hash mapping solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # initialize the hash map
        hash_map = {}  
        
        # iterate through the array
        for i, num in enumerate(nums):  
            
            # calculate complement
            complement = target - num  
            
            # check if complement exists
            if complement in hash_map:  
                # Return indices of complement and current element
                return [hash_map[complement], i]  
            
            # store the element with its index
            hash_map[num] = i  


# solution with two pointers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # sort original indices
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])  
        
        # initialize pointers
        left, right = 0, len(nums) - 1 
        
        # iterate with two pointers
        while left < right: 
            current_sum = sorted_nums[left][1] + sorted_nums[right][1]
            
            # check for the target sum
            if current_sum == target:  
                return [sorted_nums[left][0], sorted_nums[right][0]]
            elif current_sum < target:
                
                # move left pointer to the right
                left += 1  
            else:
                
                # move right pointer to the left
                right -= 1  
        
        # return an empty list if no solution is found
        return [] 