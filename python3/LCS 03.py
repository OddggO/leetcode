from typing import List

class Solution:
    def dfs(self, grid: List[str], flag: List[int], first: str, i: int, j: int) -> int:
        if i < 0 or i >= len(grid):
            return -1
        if j < 0 or j >= len(grid[i]):
            return -1
        if grid[i][j] == "0":
            return -1
                    
        if grid[i][j] != first or flag[i][j] == 1:
            return 0
        
        flag[i][j] = 1
        r0 = self.dfs(grid, flag, first, i, j + 1)
        r1 = self.dfs(grid, flag, first, i, j - 1)
        r2 = self.dfs(grid, flag, first, i + 1, j)
        r3 = self.dfs(grid, flag, first, i - 1, j)
        r = [r0, r1, r2, r3]
        return -1 if -1 in r else sum(r) + 1
    
    def largestArea(self, grid: List[str]) -> int: 
        ans = 0
        flag = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ret = self.dfs(grid, flag, grid[i][j], i, j)
                if grid[i][j] != '0':
                    ans = max(ans, ret)
                    
                # print(i, j, grid[i][j], ret, ans)
                    
        return ans