#
# Problem: 1545. Find Kth Bit in Nth Binary String
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/1936985887/?envType=daily-question&envId=2026-03-03
# Language: python3
# Date: 2026-03-03


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        sequence = "0"
        for i in range(1, n):
            if k <= len(sequence):
                break
            sequence += "1"
            inverted = "".join(
                "1" if bit == "0" else "0" for bit in sequence[:-1]
            )
            sequence += inverted[::-1]
        return sequence[k - 1]
