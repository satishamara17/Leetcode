#
# Problem: 3742. Maximum Path Score in a Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-path-score-in-a-grid/submissions/1992064895/?envType=daily-question&envId=2026-04-30
# Language: python3
# Date: 2026-04-30


class Solution:
    def maxPathScore(self, grid, k):
        m = len(grid)      # m stores number of rows
        n = len(grid[0])   # n stores number of columns
        neg = -1           # neg is used for unreachable states

        dp = [[[neg] * (k + 1) for _ in range(n)] for _ in range(m)]  # dp[r][c][cost] stores best score at cell with exact cost
        dp[0][0][0] = 0  # start cell has value 0, so initial score and cost are 0

        for r in range(m):  # loop through each row
            for c in range(n):  # loop through each column
                for cost in range(k + 1):  # loop through all possible costs
                    if dp[r][c][cost] == neg:
                        continue

                    if r + 1 < m:
                        val = grid[r + 1][c]          # val stores next cell value
                        add_cost = 0 if val == 0 else 1  # add_cost stores cost of entering next cell
                        new_cost = cost + add_cost    # new_cost stores total cost after moving
                        if new_cost <= k:
                            dp[r + 1][c][new_cost] = max(dp[r + 1][c][new_cost], dp[r][c][cost] + val)

                    if c + 1 < n:
                        val = grid[r][c + 1]          # val stores next cell value
                        add_cost = 0 if val == 0 else 1  # add_cost stores cost of entering next cell
                        new_cost = cost + add_cost    # new_cost stores total cost after moving
                        if new_cost <= k:
                            dp[r][c + 1][new_cost] = max(dp[r][c + 1][new_cost], dp[r][c][cost] + val)

        return max(dp[m - 1][n - 1])  # max is used to get best score among all costs within k
