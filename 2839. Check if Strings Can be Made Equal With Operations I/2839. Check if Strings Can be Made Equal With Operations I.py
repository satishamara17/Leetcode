#
# Problem: 2839. Check if Strings Can be Made Equal With Operations I
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/submissions/1966265001/?envType=daily-question&envId=2026-03-29
# Language: python3
# Date: 2026-04-01


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return ({s1[0], s1[2]} == {s2[0], s2[2]} and
                {s1[1], s1[3]} == {s2[1], s2[3]})
