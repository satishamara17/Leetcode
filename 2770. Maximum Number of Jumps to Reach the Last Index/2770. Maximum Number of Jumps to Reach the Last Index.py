#
# Problem: 2770. Maximum Number of Jumps to Reach the Last Index
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/submissions/2000063015/?envType=daily-question&envId=2026-05-10
# Language: python3
# Date: 2026-05-10


class Solution:  # class is used because the platform expects the method inside Solution
    def maximumJumps(self, nums: List[int], target: int) -> int:  # def is used to define the required function
        n = len(nums)  # number of elements in nums
        dp = [-1] * n  # maximum jumps needed to reach each index, -1 means not reachable

        dp[0] = 0  # starting index needs 0 jumps to reach itself

        for i in range(n):  # range is used to visit every index from left to right
            if dp[i] == -1:
                continue  # continue is used to skip unreachable indices

            for j in range(i + 1, n):  # range is used to check every future index
                diff = nums[j] - nums[i]  # value difference between destination and current index

                if -target <= diff <= target:
                    cur = dp[i] + 1  # jumps needed if I jump from i to j

                    if cur > dp[j]:
                        dp[j] = cur

        return dp[n - 1]
