#
# Problem: 3212. Count Submatrices With Equal Frequency of X and Y
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/submissions/1953195617/?envType=daily-question&envId=2026-03-19
# Language: python3
# Date: 2026-03-19


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n ,m = len(grid), len(grid[0])
        colX = [0]*m
        colY = [0]*m
        ans=0
        for i in range(n):
            numX = 0
            numY = 0 
            for j in range(m):
                if grid[i][j]== 'X':
                    colX[j]+=1
                elif grid[i][j] == 'Y':
                    colY[j]+=1

                numX += colX[j]
                numY += colY[j]

                if numX == numY and numX != 0:
                    ans+=1
        return ans
