from typing import List
import sys
from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = [[sys.maxsize] * m for _ in range(n)]
        q = deque()
        q.append((0, 0))
        dist[0][0] = grid[0][0]
        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    cost = grid[x][y]
                    if dist[i][j] + cost < dist[x][y]:
                        dist[x][y] = dist[i][j] + cost
                        if cost == 0:
                            q.appendleft((x, y))
                        else:
                            q.append((x, y))
                            
        return dist[-1][-1]    
