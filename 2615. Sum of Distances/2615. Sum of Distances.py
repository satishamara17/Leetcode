#
# Problem: 2615. Sum of Distances
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-of-distances/submissions/1986520001/?envType=daily-question&envId=2026-04-23
# Language: python3
# Date: 2026-04-23


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = defaultdict(list)  # mp stores each value with all its indices
        n = len(nums)           # n stores length of nums

        for i, x in enumerate(nums):  # enumerate is used to get index and value together
            mp[x].append(i)           # append adds current index to that value group

        ans = [0] * n  # ans stores final distance sum for every index

        for arr in mp.values():       # values is used to process each index group
            total = sum(arr)          # total stores sum of all indices in this group
            left = 0                  # left stores sum of indices already processed

            for k, cur in enumerate(arr):  # k is count of processed indices, cur is current original index
                lc = k                     # lc stores count of indices on left side
                rc = len(arr) - k - 1      # rc stores count of indices on right side

                ans[cur] = cur * lc - left + total - left - cur - cur * rc
                left += cur                # updates processed index sum

        return ans
