#
# Problem: 796. Rotate String
# Difficulty: Easy
# Link: https://leetcode.com/problems/rotate-string/submissions/1994355169/?envType=daily-question&envId=2026-05-03
# Language: python3
# Date: 2026-05-03


class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):  # len is used to check both strings have same length
            return False

        return goal in (s + s)  # in is used to check whether goal appears as a rotation inside doubled s
