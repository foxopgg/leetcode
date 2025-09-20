class Solution(object):
    def rotate(self, matrix):
        length = len(matrix)

        for i in range(length):
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(0, length):
            start = 0
            end = length - 1
            while start < end:
                matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                start += 1
                end -= 1