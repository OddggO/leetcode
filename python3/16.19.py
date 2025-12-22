from typing import List

class Solution:
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if i < 0 or i >= len(grid):
            return 0
        if j <0 or j >= len(grid[i]):
            return 0
        if grid[i][j] != 0:
            return 0
        ret = 1
        grid[i][j] = 1
        ret += self.dfs(grid, i, j + 1)
        ret += self.dfs(grid, i, j - 1)
        ret += self.dfs(grid, i + 1, j)
        ret += self.dfs(grid, i - 1, j)
        ret += self.dfs(grid, i - 1, j - 1)
        ret += self.dfs(grid, i - 1, j + 1)
        ret += self.dfs(grid, i + 1, j - 1)
        ret += self.dfs(grid, i + 1, j + 1)
        return ret
    
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(land)):
            for j in range(len(land[i])):
                s = self.dfs(land, i, j)
                # print(i, j, s)
                if s:
                    res.append(s)
                
        res.sort()
        # print(res)
        return res