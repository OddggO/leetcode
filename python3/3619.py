from typing import List

class Solution:
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if i < 0 or i >= len(grid):
            return 0
        if j <0 or j >= len(grid[i]):
            return 0
        if grid[i][j] == 0:
            return 0
        ret = grid[i][j]
        grid[i][j] = 0
        ret += self.dfs(grid, i, j + 1)
        ret += self.dfs(grid, i, j - 1)
        ret += self.dfs(grid, i + 1, j)
        ret += self.dfs(grid, i - 1, j)
        return ret
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ret = self.dfs(grid, i, j)
                if ret and ret % k == 0:
                    res += 1
                
        return res