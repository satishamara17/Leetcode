#
# Problem: 3418. Maximum Amount of Money Robot Can Earn
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/submissions/1966893987/?envType=daily-question&envId=2026-04-02
# Language: python3
# Date: 2026-04-02


from math import inf  # used for a very small starting value by taking -inf


class Solution:
    def maximumAmount(self, coins):
        m = len(coins)  # number of rows
        n = len(coins[0])  # number of columns
        neg = -inf  # impossible state marker

        dp = [[[neg] * 3 for _ in range(n)] for _ in range(m)]  # dp[i][j][k] = best coins at cell (i,j) using k neutralizations

        v = coins[0][0]  # value at starting cell
        dp[0][0][0] = v  # start without using neutralization
        if v < 0:  # only robber cells can be neutralized
            dp[0][0][1] = 0  # start by neutralizing the robber at (0,0)

        for i in range(m):  # iterate through each row
            for j in range(n):  # iterate through each column
                if i == 0 and j == 0:  # base cell already initialized
                    continue

                v = coins[i][j]  # current cell value

                for k in range(3):  # k = number of neutralizations used so far
                    best = neg  # best value for current state

                    if i > 0 and dp[i - 1][j][k] != neg:  # come from top without changing k
                        best = max(best, dp[i - 1][j][k] + v)  # take current cell normally

                    if j > 0 and dp[i][j - 1][k] != neg:  # come from left without changing k
                        best = max(best, dp[i][j - 1][k] + v)  # take current cell normally

                    if v < 0 and k > 0:  # can neutralize only if current cell is robber and one neutralization is available
                        if i > 0 and dp[i - 1][j][k - 1] != neg:  # come from top and use neutralization here
                            best = max(best, dp[i - 1][j][k - 1])  # add 0 because robbery is prevented

                        if j > 0 and dp[i][j - 1][k - 1] != neg:  # come from left and use neutralization here
                            best = max(best, dp[i][j - 1][k - 1])  # add 0 because robbery is prevented

                    dp[i][j][k] = best  # store the best possible value for this state

        return max(dp[m - 1][n - 1])  # best answer at destination with 0, 1, or 2 neutralizations used
