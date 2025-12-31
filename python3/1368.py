from typing import List
import sys
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 0 + 1, 1 + 1, 2 + 1, 3 + 1 = 1, 2, 3, 4
        dist = [[sys.maxsize] * m for _ in range(n)]
        q = deque()
        q.append((0, 0))
        dist[0][0] = 0
        while q:
            i, j = q.popleft()
            for d, (dx, dy) in enumerate(directions):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    cost = int(grid[i][j] != d + 1)
                    if dist[i][j] + cost < dist[x][y]:
                        dist[x][y] = dist[i][j] + cost
                        if cost == 0:
                            q.appendleft((x, y))
                        else:
                            q.append((x, y))
                            
        return dist[-1][-1]    