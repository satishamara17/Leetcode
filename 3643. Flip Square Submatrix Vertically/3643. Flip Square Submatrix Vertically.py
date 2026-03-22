#
# Problem: 3643. Flip Square Submatrix Vertically
# Difficulty: Easy
# Link: https://leetcode.com/problems/flip-square-submatrix-vertically/submissions/1955936156/?envType=daily-question&envId=2026-03-21
# Language: python3
# Date: 2026-03-22


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        i0, i1 = x, x + k - 1
        while i0 < i1:
            for j in range(y, y + k):
                grid[i0][j], grid[i1][j] = grid[i1][j], grid[i0][j]
            i0, i1 = i0 + 1, i1 - 1
        return grid
