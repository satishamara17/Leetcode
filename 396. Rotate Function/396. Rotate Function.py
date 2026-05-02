#
# Problem: 396. Rotate Function
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-function/submissions/1993668288/?envType=daily-question&envId=2026-05-01
# Language: python3
# Date: 2026-05-02


class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)  # n stores the length of nums
        total = sum(nums)  # total stores sum of all numbers
        cur = 0  # cur stores current rotation function value

        for i, x in enumerate(nums):  # enumerate is used to get index and value together
            cur += i * x

        ans = cur  # ans stores maximum rotation function value found so far

        for k in range(1, n):  # range is used to calculate rotations from 1 to n - 1
            cur = cur + total - n * nums[n - k]  # updates F(k) from F(k - 1)
            ans = max(ans, cur)  # max is used to keep the best value

        return ans
