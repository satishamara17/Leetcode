#
# Problem: 657. Robot Return to Origin
# Difficulty: Easy
# Link: https://leetcode.com/problems/robot-return-to-origin/submissions/1969037482/?envType=daily-question&envId=2026-04-05
# Language: python3
# Date: 2026-04-05


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0  # tracks horizontal position (right positive, left negative)
        y = 0  # tracks vertical position (up positive, down negative)

        for ch in moves:  # iterate over each move in the string
            if ch == 'U':  # move up
                y += 1  # increase vertical position
            elif ch == 'D':  # move down
                y -= 1  # decrease vertical position
            elif ch == 'L':  # move left
                x -= 1  # decrease horizontal position
            else:  # ch == 'R'
                x += 1  # increase horizontal position

        return x == 0 and y == 0  # returns True if back at origin, else False
