#
# Problem: 874. Walking Robot Simulation
# Difficulty: Medium
# Link: https://leetcode.com/problems/walking-robot-simulation/submissions/1970399479/?envType=daily-question&envId=2026-04-06
# Language: python3
# Date: 2026-04-06


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))  # stores obstacle positions for O(1) lookup
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direction vectors: north, east, south, west
        d = 0  # current direction index, starts at north
        x = 0  # current x-coordinate
        y = 0  # current y-coordinate
        ans = 0  # maximum squared distance seen so far

        for cmd in commands:  # iterate through each command
            if cmd == -2:  # turn left
                d = (d + 3) % 4  # rotate direction index left using modulo
            elif cmd == -1:  # turn right
                d = (d + 1) % 4  # rotate direction index right using modulo
            else:  # move forward cmd steps
                dx, dy = dirs[d]  # current movement direction
                for _ in range(cmd):  # move one unit at a time as required
                    nx = x + dx  # next x-coordinate
                    ny = y + dy  # next y-coordinate
                    if (nx, ny) in obs:  # stop this command if next cell has an obstacle
                        break
                    x, y = nx, ny  # update position after successful step
                    ans = max(ans, x * x + y * y)  # update maximum squared distance

        return ans  # return the farthest squared distance reached
