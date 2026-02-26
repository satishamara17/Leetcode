#
# Problem: 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/submissions/1932151351/?envType=daily-question&envId=2026-02-26
# Language: python3
# Date: 2026-02-26


class Solution:
    def numSteps(self, s: str) -> int:
        N = len(s)

        operations = 0
        carry = 0
        for i in range(N - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                operations += 2
                carry = 1
            else:
                operations += 1

        return operations + carry
