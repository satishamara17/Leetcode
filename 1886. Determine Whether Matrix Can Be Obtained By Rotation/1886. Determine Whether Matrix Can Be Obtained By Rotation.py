#
# Problem: 1886. Determine Whether Matrix Can Be Obtained By Rotation
# Difficulty: Easy
# Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/submissions/1955910265/?envType=daily-question&envId=2026-03-22
# Language: python3
# Date: 2026-03-22


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for row in mat:
                row.reverse()

            return mat
        for i in range(4):
            if rotate(mat) == target:
                return True

        return False
