#
# Problem: 1784. Check if Binary String Has at Most One Segment of Ones
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/submissions/1940036897/?envType=daily-question&envId=2026-03-06
# Language: python3
# Date: 2026-03-06


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
        
