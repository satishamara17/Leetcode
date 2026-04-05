#
# Problem: 2075. Decode the Slanted Ciphertext
# Difficulty: Medium
# Link: https://leetcode.com/problems/decode-the-slanted-ciphertext/submissions/1969038419/?envType=daily-question&envId=2026-04-04
# Language: python3
# Date: 2026-04-05


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)  # total number of characters in encoded string

        if n == 0:  # if input is empty
            return ""  # return empty string

        cols = n // rows  # number of columns in the matrix

        res = []  # list to collect decoded characters

        for c in range(cols):  # start from each column in first row
            r = 0  # start row index
            j = c  # current column index

            while r < rows and j < cols:  # traverse diagonally
                idx = r * cols + j  # convert (r, j) to index in encodedText
                res.append(encodedText[idx])  # append that character
                r += 1  # move down one row
                j += 1  # move right one column

        return "".join(res).rstrip()  # join characters and remove trailing spaces
