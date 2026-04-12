#
# Problem: 1320. Minimum Distance to Type a Word Using Two Fingers
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/submissions/1976802607/?envType=daily-question&envId=2026-04-12
# Language: python3
# Date: 2026-04-12


class Solution:
    def minimumDistance(self, word: str) -> int:
        def pos(c):
            x = ord(c) - ord('A')  # x stores letter index from 0 to 25 using ord to convert char to number
            return x // 6, x % 6  # returning row and column using // and % to map into keyboard grid

        def dist(a, b):
            ax, ay = pos(a)  # ax, ay store coordinates of first letter
            bx, by = pos(b)  # bx, by store coordinates of second letter
            return abs(ax - bx) + abs(ay - by)  # abs is used for Manhattan distance

        n = len(word)  # n stores length of the word
        dp = [0] * 26  # dp[j] stores min cost when previous typed letter uses one finger and other finger is at letter j

        for i in range(1, n):
            cur = word[i]  # cur stores current letter to type
            prev = word[i - 1]  # prev stores previous typed letter
            move = dist(prev, cur)  # move stores cost if same finger types current letter
            ndp = [float('inf')] * 26  # ndp stores next dp state, float('inf') is used as initial impossible large value

            for j in range(26):
                ndp[j] = dp[j] + move  # keeping idle finger at j and moving the active finger from prev to cur

            p = ord(prev) - ord('A')  # p stores index of previous letter, ord is used to convert char to number

            for j in range(26):
                ch = chr(j + ord('A'))  # ch stores letter for idle finger position, chr is used to convert number back to char
                cand = dp[j] + dist(ch, cur)  # cand stores cost if idle finger types current letter

                if cand < ndp[p]:
                    ndp[p] = cand  # after switching, idle finger becomes the old active finger at prev

            dp = ndp  # moving to next state

        return min(dp)  # min is used to get the best final cost among all idle finger positions
        
