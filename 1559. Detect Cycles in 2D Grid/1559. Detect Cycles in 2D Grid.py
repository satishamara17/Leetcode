#
# Problem: 1559. Detect Cycles in 2D Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/detect-cycles-in-2d-grid/submissions/1988677491/?envType=daily-question&envId=2026-04-26
# Language: python3
# Date: 2026-04-26


class Solution:
    def containsCycle(self, grid):
        m = len(grid)     # m stores number of rows
        n = len(grid[0])  # n stores number of columns

        seen = [[False] * n for _ in range(m)]  # seen stores whether a cell is already visited

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # dirs stores four possible movement directions

        def dfs(r, c, pr, pc):
            seen[r][c] = True  # mark current cell as visited

            for dr, dc in dirs:  # loop through all four directions
                nr = r + dr      # nr stores next row
                nc = c + dc      # nc stores next column

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if grid[nr][nc] != grid[r][c]:
                    continue

                if not seen[nr][nc]:
                    if dfs(nr, nc, r, c):
                        return True
                elif nr != pr or nc != pc:
                    return True

            return False

        for r in range(m):      # loop through every row
            for c in range(n):  # loop through every column
                if not seen[r][c]:
                    if dfs(r, c, -1, -1):
                        return True

        return False
