# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Initialize 'last' with the last string of 'strs' or an empty string if 'strs' is empty
        last = '' if not strs else strs.pop()

        # Iterate over each character and its index in 'last'
        for i, c in enumerate(last):
            
            # Check each string 's' in the remaining list 'strs'
            for s in strs:
                
                # If the current index 'i' is out of bounds for 's' or characters at 'i' don't match
                if i >= len(s) or s[i] != c:
                    
                    # Return the longest common prefix found so far
                    return last[:i]
        
        # If no early return occurred, 'last' is the common prefix for all strings in 'strs'
        return last
