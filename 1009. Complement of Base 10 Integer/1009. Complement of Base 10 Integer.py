#
# Problem: 1009. Complement of Base 10 Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/complement-of-base-10-integer/submissions/1944584882/?envType=daily-question&envId=2026-03-11
# Language: python3
# Date: 2026-03-11


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        mask = n
        for i in (1, 2, 4, 8, 16):
            mask |= mask >> i
        return ~n & mask
