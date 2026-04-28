#
# Problem: 2033. Minimum Operations to Make a Uni-Value Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/submissions/1989816140/?envType=daily-question&envId=2026-04-28
# Language: python3
# Date: 2026-04-28


class Solution:
    def minOperations(self, grid, x):
        arr = []  # arr stores all grid values in one flat list

        for row in grid:  # for-loop is used to scan each row
            for val in row:  # nested loop is used to scan each value inside the row
                arr.append(val)  # append is used to add current value into flat list

        rem = arr[0] % x  # rem stores the required remainder for all values

        for val in arr:  # for-loop is used to check whether all values are reachable
            if val % x != rem:
                return -1

        arr.sort()  # sort is used so that I can pick the median value
        median = arr[len(arr) // 2]  # median stores the best target value for minimum operations

        ans = 0  # ans stores total number of operations

        for val in arr:  # for-loop is used to calculate operations for every value
            ans += abs(val - median) // x  # abs gives distance from target, division by x gives operation count

        return ans
