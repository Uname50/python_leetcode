# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize the start and end indices for the longest palindrome found
        start, end = 0, 0

        # Use two pointers, i and j, to explore the string
        i, j = 0, 0

        # Continue until j reaches the end of the string
        while j < len(s):  

            # Initialize left and right pointers for the current substring
            left, right = i, j  

            # Expand around the center (left and right pointers) and check for palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                # If the current palindrome is longer than the one found before, update start and end
                if right - left > end - start:
                    start, end = left, right

                # Move left pointer one step back and right pointer one step forward
                left -= 1
                right += 1

            # If i and j are pointing at the same character, move j to the next character
            # This changes the center for the next palindrome check
            if i == j:
                j += 1
            else:
                i += 1  # Otherwise, move i one step forward to change the center

        # Return the longest palindrome substring found
        return s[start:end+1]
