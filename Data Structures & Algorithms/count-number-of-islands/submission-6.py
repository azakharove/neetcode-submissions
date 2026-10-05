class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # graph function recursive
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        neighbors = [(1,0), (-1,0), (0, 1), (0, -1)]
        islands = 0

        def search_graph(row, column):
            if row < 0 or column < 0 or row >= rows or column >= columns:
                return
            elif grid[row][column] == "0" or (row,column) in visited:
                return
            visited.add((row,column))
            for gr, gc in neighbors:
                search_graph(row + gr, column +gc)
            
        #kick it off
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row,column) not in visited:
                    search_graph(row, column)
                    islands += 1
        return islands
            