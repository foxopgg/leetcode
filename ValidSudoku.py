class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range (9)]

        for x in range(9):
            for y in range(9):
                value = board[x][y]
                if value != ".":
                    index = x // 3 * 3 + y // 3
                    if value in rows[x] or value in columns[y] or value in squares[index]:
                        return False
                    rows[x].add(value)
                    columns[y].add(value)
                    squares[index].add(value)
        return True