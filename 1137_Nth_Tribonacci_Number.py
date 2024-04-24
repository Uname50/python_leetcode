# https://leetcode.com/problems/n-th-tribonacci-number/?envType=daily-question&envId=2024-04-24

def tribonacci(n):
    
    # Base cases that are defined in the description
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    # The given values of the first 3 values
    t0, t1, t2 = 0, 1, 1
    
    # Calculate up to Tn 
    for i in range(3, n+1):

        # The current Tribonacci number is the sum of the previous 3 numbers
        current = t0 + t1 + t2

        # Shift the previous three numbers
        t0, t1, t2 = t1, t2, current
        
    # Return the nth Tribonacci number
    return t2  
