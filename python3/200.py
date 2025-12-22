from typing import List

class Solution:
    def dfs(self, grid: List[List[str]], i, j):
        # print(f"dfs, ({i}, {j})")
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = 0
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j - 1)
            return
        return # 0 # 1 if self.dfs(grid, i + 1, j) else self.dfs(grid, i, j + 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print(i, j, res)
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
                
        return res