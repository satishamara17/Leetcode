#
# Problem: 2078. Two Furthest Houses With Different Colors
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-furthest-houses-with-different-colors/submissions/1987236829/?envType=daily-question&envId=2026-04-20
# Language: python3
# Date: 2026-04-24


class Solution:
    def maxDistance(self, colors):
        n = len(colors)  # n stores the length of the array
        ans = 0          # ans stores the maximum distance found

        for j in range(n - 1, -1, -1):  # loop from right to left
            if colors[j] != colors[0]:
                ans = j                # distance from index 0 to j is j
                break

        for i in range(n):             # loop from left to right
            if colors[i] != colors[n - 1]:
                ans = max(ans, n - 1 - i)  # compare with distance from i to last index
                break

        return ans
