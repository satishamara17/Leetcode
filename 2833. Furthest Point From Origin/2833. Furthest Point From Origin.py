#
# Problem: 2833. Furthest Point From Origin
# Difficulty: Easy
# Link: https://leetcode.com/problems/furthest-point-from-origin/submissions/1986633891/?envType=daily-question&envId=2026-04-24
# Language: python3
# Date: 2026-04-24


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0   # left stores count of 'L' moves
        right = 0  # right stores count of 'R' moves
        blank = 0  # blank stores count of '_' moves

        for c in moves:  # for-loop is used to scan every move once
            if c == 'L':
                left += 1
            elif c == 'R':
                right += 1
            else:
                blank += 1

        return abs(right - left) + blank  # abs is used to get current distance, then '_' pushes it further
