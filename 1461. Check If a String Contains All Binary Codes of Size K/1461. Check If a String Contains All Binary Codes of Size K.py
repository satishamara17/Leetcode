#
# Problem: 1461. Check If a String Contains All Binary Codes of Size K
# Difficulty: Medium
# Link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23
# Language: python3
# Date: 2026-02-23


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        hasher = {}
        count=0
        for i in range(n-k+1):
            if hasher.get(s[i:i+k]) == None:
                count+=1
                hasher[s[i:i+k]]=1
        # print(count)
        return count == 2**k

