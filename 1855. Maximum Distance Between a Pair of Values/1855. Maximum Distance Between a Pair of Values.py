#
# Problem: 1855. Maximum Distance Between a Pair of Values
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/submissions/1987238526/?envType=daily-question&envId=2026-04-19
# Language: python3
# Date: 2026-04-24


class Solution:
    def maxDistance(self, nums1, nums2):
        i = 0   # i is pointer for nums1
        j = 0   # j is pointer for nums2
        ans = 0 # ans stores maximum distance

        n1 = len(nums1) # length of nums1
        n2 = len(nums2) # length of nums2

        while i < n1 and j < n2: # loop until any pointer goes out of bounds
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i) # update maximum distance if valid pair
                j += 1                # move j forward to try larger distance
            else:
                i += 1                # move i forward to satisfy condition

        return ans
