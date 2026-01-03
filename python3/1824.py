from typing import List
from collections import deque
import sys

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n, m = len(obstacles) - 1, 3
        grid = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacles[i] == j + 1:
                    grid[i][j] = True
        dist = [[sys.maxsize] * 3 for _ in range(n)] # 每个坐标最小侧跳次数
        dist[1][0] = 0
        directions = [(0, 1), (1, 0), (2, 0), (-1, 0), (-1, 0)]
        q = deque()
        q.append((1, 0))

        while q:
            i, j = q.popleft()
            if i == n:
                return dist[i][j]
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not grid[x][y]:
                    if dx == 0:
                        cost = 0
                        q.appendleft((x, y))
                    else:
                        cost = 1
                        q.append((x, y))
                    if dist[i][j] + cost < dist[x][y]:
                        dist[x][y] = dist[i][j] + cost

        return grid[0][-1]