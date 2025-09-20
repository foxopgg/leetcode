class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rows = [""] * numRows
        j, d = 0, 1
        for i in range(len(s)):
            rows[j] += s[i]
            if j == numRows - 1:
                d = -1
            elif j == 0:
                d = 1
            j += d
        return ''.join(rows)