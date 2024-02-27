"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)

        # if needle is empty, return 0 (found at the beginning)
        if n == 0: return 0

        # if haystack is shorter than needle, needle can't be found
        if h < n: return -1

        i, next_ = 0, [0] * n

        for j in range(1, n):
            while i > 0 and needle[i] != needle[j]:
                i = next_[i - 1]
            # if the characters match, move to the next character
            i += needle[i] == needle[j]
            # update the "next" array with the current index
            next_[j] = i

        # reset index
        i = 0

        # search through haystack using the KMP algorithm
        for j in range(h):
            # backtrack if the current character does not match
            while i > 0 and needle[i] != haystack[j]:
                i = next_[i - 1]
            # move to the next character if it matches
            i += needle[i] == haystack[j]
            # if the entire needle has been found, return the start index in haystack
            if i == n: return j - i + 1

        # if needle is not found in haystack, return -1
        return -1


sol = Solution()
haystack = "potatoes"
needle = "pot"
print(f"Index of '{needle}' in '{haystack}':", sol.strStr(haystack, needle))
