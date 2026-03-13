#
# Problem: 3296. Minimum Number of Seconds to Make Mountain Height Zero
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/submissions/1947055405/?envType=daily-question&envId=2026-03-13
# Language: python3
# Date: 2026-03-13


class Solution:
    def minNumberOfSeconds(
        self, mountainHeight: int, workerTimes: List[int]
    ) -> int:
        maxWorkerTimes = max(workerTimes)
        l, r, ans = (
            1,
            maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2,
            0,
        )
        eps = 1e-7

        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for t in workerTimes:
                work = mid // t
                # find the largest k such that 1+2+...+k <= work
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2 + eps)
                cnt += k
            if cnt >= mountainHeight:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
