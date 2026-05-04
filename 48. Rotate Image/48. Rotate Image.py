#
# Problem: 48. Rotate Image
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-image/submissions/1995049478/?envType=daily-question&envId=2026-05-04
# Language: python3
# Date: 2026-05-04


class Solution:
    def rotate(self, matrix):
        n = len(matrix)  # n stores the size of the square matrix

        for r in range(n):  # range is used to go through each row index
            for c in range(r + 1, n):  # range starts from r + 1 to avoid swapping diagonal and duplicate pairs
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]  # tuple assignment swaps two values in-place

        for row in matrix:  # for-loop is used to visit each row
            row.reverse()  # reverse is used to reverse the row in-place
