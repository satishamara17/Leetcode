#
# Problem: 788. Rotated Digits
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotated-digits/submissions/1993666083/?envType=daily-question&envId=2026-05-02
# Language: python3
# Date: 2026-05-02


class Solution:
    def rotatedDigits(self, n):
        ans = 0  # ans stores count of good numbers

        for num in range(1, n + 1):  # range is used to check every number from 1 to n
            x = num        # x stores current number while checking digits
            changed = False  # changed tells whether at least one digit changes after rotation
            valid = True     # valid tells whether all digits can rotate into valid digits

            while x > 0:
                d = x % 10  # d stores the last digit of x

                if d == 3 or d == 4 or d == 7:
                    valid = False
                    break

                if d == 2 or d == 5 or d == 6 or d == 9:
                    changed = True

                x //= 10  # integer division removes the last digit

            if valid and changed:
                ans += 1

        return ans
