from typing import List
from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    q.append((i, j))
                    
        if not q or len(q) == 0 or len(q) == n * m:
            return -1
        ans = 0
        while q:
            for _ in range(len(q)): # 记录当前这一层有多少元素，这样可以避免复制队列
                i, j = q.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and not grid[x][y]:
                        q.append((x, y))
                        grid[x][y] = 1
            ans += 1
        return ans - 1
    
    # def clear(self):
    #     for i in range(self.n):
    #         for j in range(self.m):
    #             self.flag[i][j] = False
    
    # def bfs(self, i, j):
    #     self.clear()
    #     q = deque()
    #     q.append((i, j, 0))
    #     self.flag[i][j] = True
    #     while len(q):
    #         i, j, v = q.popleft()
    #         for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
    #             if 0 <= x < self.n and 0 <= y < self.m and not self.flag[x][y]:
    #                 if self.grid[x][y] == 1:
    #                     return v + 1
    #                 self.flag[x][y] = True
    #                 q.append((x, y, v + 1))
                    
                    
    #     return -1
        
    # def maxDistance(self, grid: List[List[int]]) -> int:
    #     n, m = len(grid), len(grid[0])
    #     self.grid = grid
    #     self.n, self.m = n, m
    #     self.flag = [[False] * m for _ in range(n)]
    #     ans = -1
    #     for i in range(n):
    #         for j in range(m):
    #             if not grid[i][j]: # == 0
    #                 ans = max(ans, self.bfs(i, j))
                    
    #     return ans

                