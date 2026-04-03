#
# Problem: 3661. Maximum Walls Destroyed by Robots
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximum-walls-destroyed-by-robots/submissions/1967977580/?envType=daily-question&envId=2026-04-03
# Language: python3
# Date: 2026-04-03


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        arr = sorted(zip(robots, distance))  # pairs each robot with its range and sorts by robot position
        ws = sorted(walls)  # sorts wall positions for binary-search counting
        n = len(arr)  # number of robots

        def cnt(l, r):
            if l > r:  # empty interval cannot destroy any wall
                return 0
            i = bisect_left(ws, l)  # first wall position >= l
            j = bisect_right(ws, r)  # first wall position > r
            return j - i  # number of walls inside [l, r]

        seg = []  # seg[i] = [(left_l, left_r), (right_l, right_r)] for robot i
        val = []  # val[i] = [walls destroyed by left shot, walls destroyed by right shot]

        for i, (x, d) in enumerate(arr):
            ll = x - d  # natural left reach without blocker
            rr = x + d  # natural right reach without blocker

            if i > 0:
                ll = max(ll, arr[i - 1][0] + 1)  # left bullet cannot cross previous robot

            if i + 1 < n:
                rr = min(rr, arr[i + 1][0] - 1)  # right bullet cannot cross next robot

            left_seg = (ll, x)  # interval covered if this robot shoots left
            right_seg = (x, rr)  # interval covered if this robot shoots right
            seg.append([left_seg, right_seg])  # stores both choices for this robot
            val.append([cnt(ll, x), cnt(x, rr)])  # precomputes walls destroyed by each choice

        prev = [val[0][0], val[0][1]]  # dp for first robot: choose left or choose right

        for i in range(1, n):
            cur = [-10**18, -10**18]  # current dp values for choosing left or right on robot i

            for p in range(2):  # previous robot choice: 0 = left, 1 = right
                pl, pr = seg[i - 1][p]  # previous interval boundaries

                for c in range(2):  # current robot choice: 0 = left, 1 = right
                    cl, cr = seg[i][c]  # current interval boundaries
                    ol = max(pl, cl)  # left boundary of overlap
                    orr = min(pr, cr)  # right boundary of overlap
                    overlap = cnt(ol, orr) if ol <= orr else 0  # walls counted by both intervals
                    cur[c] = max(cur[c], prev[p] + val[i][c] - overlap)  # add new walls only once

            prev = cur  # moves dp window forward

        return max(prev)  # best result after processing all robots
