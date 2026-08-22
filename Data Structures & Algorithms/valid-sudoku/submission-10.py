from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row in range(9):
        #     seen = set()
        #     for column in range(9):
        #         cell = board[row][column]
        #         if cell in seen:
        #             return False
        #         elif cell == ".":
        #             continue
        #         else:
        #             seen.add(cell)
        # for column in range(9):
        #     seen = set()
        #     for row in range(9):
        #         cell = board[row][column]
        #         if cell in seen:
        #             return False
        #         elif cell == ".":
        #             continue
        #         else:
        #             seen.add(cell)
        # for square in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (square // 3) * 3 + i
        #             column = (square % 3) * 3 + j
        #             cell = board[row][column]
        #             if cell in seen:
        #                 return False
        #             elif cell == ".":
        #                 continue
        #             else:
        #                 seen.add(cell)
        # return True
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)        
        for row in range(9):
            for column in range(9):
                    cell = board[row][column]
                    if cell == ".":
                        continue
                    if cell in rows[row]:
                        return False
                    elif cell in cols[column]:
                        return False
                    elif cell in squares[(row//3, column//3)]:
                        return False
                    rows[row].add(cell)
                    cols[column].add(cell)
                    squares[(row//3, column//3)].add(cell)
        return True

