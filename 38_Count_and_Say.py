# https://leetcode.com/problems/count-and-say/description/ 

import itertools 

class Solution:
    def countAndSay(self, n: int) -> str:
        
        # Start the sequence with the first term being '1'
        s = '1'  

        # Repeat the process n-1 times to get to the nth term
        for _ in range(n - 1):  

            # Generate the next term in the sequence by concatenating...
            s = ''.join(

                # The count of digits 
                str(sum(map(bool, v))) + k  

                # For each group of consecutive identical digits in s
                for k, v in itertools.groupby(s)  
            )

        # Return the nth term in the sequence
        return s  