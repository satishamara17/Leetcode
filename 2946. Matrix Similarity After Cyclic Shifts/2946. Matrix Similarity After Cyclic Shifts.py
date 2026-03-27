#
# Problem: 2946. Matrix Similarity After Cyclic Shifts
# Difficulty: Easy
# Link: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/submissions/1960438565/?envType=daily-question&envId=2026-03-27
# Language: python3
# Date: 2026-03-27


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n

        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True
