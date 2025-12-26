from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        flag = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        q.append((0, 0, health - 1 if grid[0][0] else health))
        while q:
            i, j, h = q.popleft()
            if i == n - 1 and j == m - 1 and h > 0:
                return True
            flag[i][j] = True
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and not flag[x][y]:
                    # if x == n - 1 and y == m - 1 and h
                    q.append((x, y, h - 1 if grid[x][y] else h))
                    
        return False
        
    # def dfs(self, i: int, j: int, health: int):
    #     if i < 0 or i >= self.n:
    #         return -1
    #     if j < 0 or j >= self.m:
    #         return -1
    #     if i == self.n - 1 and j == self.m - 1:
    #         return health - 1 if self.grid[i][j] else health
    #     if self.flag[i][j]:
    #         return -1
    #     self.flag[i][j] = True
    #     self.dfs(i + 1, j)
    #     self.dfs(i - 1, j)
    #     self.dfs(i, j + 1)
    #     self.dfs(i, j - 1)
        
    
    # def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
    #     self.n, self.m = len(grid), len(grid[0])
    #     self.health = health
    #     self.grid = grid
    #     self.flag = [[]]