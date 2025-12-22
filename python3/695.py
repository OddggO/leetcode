from typing import List

class Solution:
    def dfs(self, grid: List[List[int]], i, j) -> int:
        # print(f"dfs, ({i}, {j})")
        if i < 0 or i >= len(grid):
            return 0
        if j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == 1:
            grid[i][j] = 0
            ret = 1
            ret += self.dfs(grid, i, j + 1)
            ret += self.dfs(grid, i + 1, j)
            ret += self.dfs(grid, i, j - 1)
            ret += self.dfs(grid, i - 1, j)
            return ret
        return 0 # 0 # 1 if self.dfs(grid, i + 1, j) else self.dfs(grid, i, j + 1)
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res = max(self.dfs(grid, i, j), res)
                
        return res