#
# Problem: 3464. Maximize the Distance Between Points on a Square
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/submissions/1987917418/?envType=daily-question&envId=2026-04-25
# Language: python3
# Date: 2026-04-25


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        arr = []  # arr stores each boundary point as one perimeter position
        p = 4 * side  # p stores total perimeter length of the square

        for x, y in points:  # loop is used to convert every 2D boundary point
            if y == 0:
                arr.append(x)  # bottom side position
            elif x == side:
                arr.append(side + y)  # right side position
            elif y == side:
                arr.append(3 * side - x)  # top side position
            else:
                arr.append(4 * side - y)  # left side position

        arr.sort()  # sort is used so I can greedily pick points in perimeter order
        n = len(arr)  # n stores number of points
        ext = arr + [x + p for x in arr]  # ext handles circular perimeter by duplicating positions

        def can(d: int) -> bool:
            for start in range(n):  # start tries each point as first selected point
                cnt = 1  # cnt stores how many points I selected
                last = ext[start]  # last stores perimeter position of last selected point
                idx = start  # idx stores index of last selected point in ext

                while cnt < k:
                    nxt = bisect_left(ext, last + d, idx + 1, start + n)  # finds next point at distance at least d
                    if nxt == start + n:
                        break
                    idx = nxt  # update index of selected point
                    last = ext[idx]  # update last selected position
                    cnt += 1  # increase selected count

                if cnt == k and ext[start] + p - last >= d:
                    return True

            return False

        low = 0  # low stores minimum possible answer
        high = side  # high stores maximum possible answer
        ans = 0  # ans stores best valid distance found

        while low <= high:
            mid = (low + high) // 2  # mid is current distance I am checking

            if can(mid):
                ans = mid  # mid is possible, so I store it
                low = mid + 1  # try for a bigger distance
            else:
                high = mid - 1  # mid is not possible, so reduce distance

        return ans
