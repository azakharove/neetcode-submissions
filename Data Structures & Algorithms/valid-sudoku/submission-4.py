class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for column in range(9):
                cell = board[row][column]
                if cell in seen:
                    return False
                elif cell == ".":
                    continue
                else:
                    seen.add(cell)
        for column in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][column]
                if cell in seen:
                    return False
                elif cell == ".":
                    continue
                else:
                    seen.add(cell)
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    column = (square % 3) * 3 + j
                    cell = board[row][column]
                    if cell in seen:
                        return False
                    elif cell == ".":
                        continue
                    else:
                        seen.add(cell)
        return True