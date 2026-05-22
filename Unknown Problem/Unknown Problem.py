#
# Problem: Unknown Problem
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/2010224043/?envType=daily-question&envId=2026-05-22
# Language: python3
# Date: 2026-05-22


class Solution:  # class is used because the platform expects the method inside Solution
    def search(self, nums: List[int], target: int) -> int:  # def is used to define the required function
        l = 0  # left boundary of the current search range
        r = len(nums) - 1  # right boundary of the current search range

        while l <= r:  # while is used because I keep shrinking the search range
            m = (l + r) // 2  # middle index of the current search range

            if nums[m] == target:
                return m  # return the index immediately when target is found

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1  # target lies in the sorted left half
                else:
                    l = m + 1  # target cannot lie in the sorted left half
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1  # target lies in the sorted right half
                else:
                    r = m - 1  # target cannot lie in the sorted right half

        return -1  # target was not found in nums
