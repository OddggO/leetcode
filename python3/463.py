from typing import List

class Solution:
    # def dfs(self, grid: List[List[int]], flag: List[List[bool]], i: int, j: int) -> int:
    #     if i < 0 or i >= len(grid):
    #         return 0
    #     if j < 0 or j >= len(grid[i]):
    #         return 0
    #     print(i, j, grid[i][j])
    #     if grid[i][j] == 0:
    #         return 0
    #     if flag[i][j]:
    #         return -1
    #     flag[i][j] = True
    #     ret = 4
    #     r = self.dfs(grid, flag, i, j + 1)
    #     ret += r if r <= 0 else r - 1
    #     r = self.dfs(grid, flag, i, j - 1)
    #     ret += r if r <= 0 else r - 1
    #     r = self.dfs(grid, flag, i + 1, j)
    #     ret += r if r <= 0 else r - 1
    #     r = self.dfs(grid, flag, i - 1, j)
    #     ret += r if r <= 0 else r - 1
    #     # print(i, j, grid[i][j], ret)
        # return ret if ret > 0 else -1 # 防止四周全是陆地的网格返回0，造成上一层无法得知这里有边界
    
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     flag = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             ret = self.dfs(grid, flag, i, j)
    #             if ret > 0:
    #                 return ret
                
    #     return 0
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ret = 0
        n, m = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    ret += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    ret += 1
                if i + 1 >= n or grid[i + 1][j] == 0:
                    ret += 1
                if j + 1 >= m or grid[i][j + 1] == 0:
                    ret += 1
        return ret
        
if __name__ == "__main__":
    grid = [[0,1,1,0],[1,1,1,1],[1,1,1,1]]
    for g in grid:
        print(g)
    s = Solution()
    ret = s.islandPerimeter(grid)
    print(ret)