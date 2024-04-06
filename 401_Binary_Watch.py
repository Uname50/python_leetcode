# https://leetcode.com/problems/binary-watch/ 

class Solution:
    def readBinaryWatch(self, turnedOn: int):
        return [f'{hh}:{mm:02}' for hh in range(12) for mm in range(60)
                                if f'{hh:b}{mm:b}'.count('1') == turnedOn]