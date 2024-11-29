# https://leetcode.com/problems/two-sum/description/ 

def twoSum_solution1(nums: list[int], target: int) -> list[int]:

    """
    Bruteforce solution. Creates 2 loops to compare every possible pair of numbers. It's inefficient, but it does the job
    """

    # First loop creates the first number to compare. It goes from 0 to (last index - 1)
    for first_number_index in range(len(nums)):
        
        # Second loop creates the second number to compare. We start from the next element after the first number, to avoid comparing the first number to itself
        for second_number_index in range(first_number_index + 1, len(nums)):  
            
            # The target was given as the function parameter. If the element of the list at the first number index + the element at the second index add up to the target, 
            # return the 2 indices as a list
            if nums[first_number_index] + nums[second_number_index] == target:
                return [first_number_index, second_number_index]
