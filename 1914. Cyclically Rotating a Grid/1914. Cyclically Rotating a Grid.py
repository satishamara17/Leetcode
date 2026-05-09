#
# Problem: 1914. Cyclically Rotating a Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/cyclically-rotating-a-grid/submissions/1999010590/?envType=daily-question&envId=2026-05-09
# Language: python3
# Date: 2026-05-09


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)  # number of rows in the grid
        n = len(grid[0])  # number of columns in the grid
        res = [row[:] for row in grid]  # final grid where I will place rotated values
        layers = min(m, n) // 2  # total number of layers in the grid

        for l in range(layers):  # I process each layer from outside to inside
            top = l  # top row index of the current layer
            left = l  # left column index of the current layer
            bottom = m - 1 - l  # bottom row index of the current layer
            right = n - 1 - l  # right column index of the current layer
            coords = []  # coordinates of the current layer in counter-clockwise order

            for r in range(top, bottom + 1):  # I move down on the left side
                coords.append((r, left))  # I add the current left-side cell

            for c in range(left + 1, right + 1):  # I move right on the bottom side
                coords.append((bottom, c))  # I add the current bottom-side cell

            for r in range(bottom - 1, top - 1, -1):  # I move up on the right side
                coords.append((r, right))  # I add the current right-side cell

            for c in range(right - 1, left, -1):  # I move left on the top side
                coords.append((top, c))  # I add the current top-side cell

            vals = [grid[r][c] for r, c in coords]  # original values of this layer
            size = len(coords)  # number of cells in this layer
            shift = k % size  # effective rotations needed for this layer

            for i in range(size):  # I place every rotated value back into this layer
                r, c = coords[i]  # current target cell
                res[r][c] = vals[(i - shift) % size]  # value coming from shift steps behind

        return res
