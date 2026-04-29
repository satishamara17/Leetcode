#
# Problem: 3225. Maximum Score From Grid Operations
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximum-score-from-grid-operations/submissions/1991203561/?envType=daily-question&envId=2026-04-29
# Language: python3
# Date: 2026-04-29


class Solution:
    def maximumScore(self, grid):
        n = len(grid)  # n stores the size of the square grid
        h = n + 1      # h stores total possible black heights from 0 to n
        neg = -10**30  # neg is used as a very small value for impossible states

        pref = [[0] * h for _ in range(n)]  # pref[c][r] stores sum of column c from row 0 to r - 1

        for c in range(n):  # loop is used to build prefix sums column-wise
            for r in range(n):  # loop is used to scan rows of current column
                pref[c][r + 1] = pref[c][r] + grid[r][c]

        def get_sum(c, a, b):
            if b <= a:
                return 0
            return pref[c][b] - pref[c][a]

        dp = [[neg] * h for _ in range(h)]  # dp[left][cur] stores best score before finalizing current column

        for cur in range(h):  # cur tries all possible height choices for first column
            dp[0][cur] = 0    # left boundary height before column 0 is 0

        for c in range(n):  # c is the current column being finalized
            ndp = [[neg] * h for _ in range(h)]  # ndp stores next DP states after finalizing column c
            rights = range(h) if c < n - 1 else [0]  # right height is 0 after the last column boundary

            for cur in range(h):  # cur is black height of current column
                vals = [dp[left][cur] for left in range(h)]  # vals stores all states for fixed current height

                best_left = [neg] * h  # best_left[r] stores best dp[left][cur] where left <= r
                best = neg             # best stores running maximum

                for r in range(h):  # r is possible right height boundary
                    best = max(best, vals[r])  # max is used to maintain best state so far
                    best_left[r] = best

                best_greater = [neg] * h  # best_greater[r] stores best value where left > r
                best = neg                # best stores running maximum for greater-left case

                for left in range(h - 1, -1, -1):  # loop from right to left to handle left > right condition
                    best_greater[left] = best
                    gain = get_sum(c, cur, left)  # gain stores contribution when left height is bigger
                    best = max(best, vals[left] + gain)

                for right in rights:  # right is black height of next column
                    gain = get_sum(c, cur, right)  # gain stores contribution when right side controls score
                    ndp[cur][right] = max(best_left[right] + gain, best_greater[right])

            dp = ndp  # move to next column state

        return max(dp[cur][0] for cur in range(h))  # final right boundary is 0, so take best ending state
