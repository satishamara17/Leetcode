#
# Problem: 3043. Find the Length of the Longest Common Prefix
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/?envType=daily-question&envId=2026-05-21
# Language: python3
# Date: 2026-05-21


class Solution:  # class is used because the platform expects the method inside Solution
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:  # def is used to define the required function
        pref = set()  # set stores all prefixes from arr1 for fast lookup

        for x in arr1:  # for is used to process every number in arr1
            s = str(x)  # string form of x so I can read digits from left to right
            cur = ""  # current prefix being built for this number

            for ch in s:  # for is used to process each digit character
                cur += ch  # extend the current prefix by one digit
                pref.add(cur)  # add stores this prefix in the set

        ans = 0  # longest common prefix length found so far

        for x in arr2:  # for is used to process every number in arr2
            s = str(x)  # string form of x so I can build its prefixes
            cur = ""  # current prefix being checked for this number

            for ch in s:  # for is used to process each digit character
                cur += ch  # extend the current prefix by one digit

                if cur in pref:  # in is used to check prefix existence in O(1) average time
                    ans = max(ans, len(cur))  # max keeps the best length, len gives current prefix length

        return ans  # return gives the final longest common prefix length
