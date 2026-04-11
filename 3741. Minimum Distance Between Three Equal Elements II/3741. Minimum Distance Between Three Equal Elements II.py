#
# Problem: 3741. Minimum Distance Between Three Equal Elements II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/submissions/1975818043/?envType=daily-question&envId=2026-04-11
# Language: python3
# Date: 2026-04-11


class Solution:
    def minimumDistance(self, nums):
        mp = defaultdict(list)  # mp[val] stores all indices where this value appears
        
        for i in range(len(nums)):
            mp[nums[i]].append(i)  # collecting indices for each value
        
        ans = float('inf')  # to track minimum distance
        
        for val in mp:
            lst = mp[val]  # list of indices for current value
            
            if len(lst) < 3:
                continue  # we need at least 3 indices
            
            for i in range(len(lst) - 2):
                left = lst[i]       # first index in triple
                right = lst[i + 2] # third index in triple
                
                dist = 2 * (right - left)  # using simplified formula
                
                if dist < ans:
                    ans = dist  # updating minimum
        
        return -1 if ans == float('inf') else ans  # return -1 if no valid triple
