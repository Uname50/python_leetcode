# https://leetcode.com/problems/largest-number/description/ 

from typing import List


class Predicate(str):
    # Override the "less than" operator
    def __lt__(self, other):
        return self + other < other + self

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert the list of ints to strings, sort them with the Predicate class, and reverse the order to get the largest number 
        strings = ''.join(sorted(map(str, nums), key=Predicate, reverse=True))
        # Check if the first character is a zero and if so, return '0'. Otherwise, return the string of sorted numbers
        return '0' if strings[0] == '0' else strings
