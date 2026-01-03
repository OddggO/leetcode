from typing import List
import sys
from collections import deque, defaultdict

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        if matrix[-1][-1] == "#":
            return -1
            
        n, m = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        dist = [[sys.maxsize] * m for _ in range(n)]
        dist[0][0] = 0
        q = deque()
        q.append((0, 0))
        portal = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if c.isupper():
                    portal[c].append((i, j))

        while q:
            i, j = q.popleft()
            d = dist[i][j]
            # if i == n - 1 and j == m - 1:
            #     return d

            c = matrix[i][j]
            
            if c in portal:
                for x, y in portal[c]:
                    if d < dist[x][y]:
                        dist[x][y] = d
                        q.appendleft((x, y))
                del portal[c]

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and c != "#" and d + 1 < dist[x][y]:
                    dist[x][y] = d + 1
                    q.append((x, y))

        return dist[-1][-1] if dist[-1][-1] != sys.maxsize else -1
    