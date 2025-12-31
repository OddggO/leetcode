from typing import List
import sys
from collections import deque

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        dist = [[sys.maxsize] * m for _ in range(n)]
        dist[0][0] = 0
        q = deque()
        q.append((0, 0))
        portal = {}
        # if "A" <= matrix[0][0] <= "Z":
        #     portal[matrix[0][0]] = (0, 0)
        while q:
            i, j = q.popleft()
            if "A" <= matrix[i][j] <= "Z" and matrix[i][j] not in portal:
                portal[matrix[i][j]] = (i, j)
            for d, (dx, dy) in enumerate(directions):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and matrix[x][y] != "#":
                    if matrix[x][y] == ".":
                        cost = 1 + dist[i][j]
                    else:
                        if matrix[x][y] in portal:
                            xx, yy = portal[matrix[x][y]]
                            if xx != -1 and yy != -1:
                                cost = 0 + dist[xx][yy]
                            else:
                                cost= 1 + dist[i][j]
                        else:
                            cost = 1 + dist[i][j]
                            portal[matrix[x][y]] = (x, y)
                    if cost < dist[x][y]:
                        dist[x][y] = cost
                        if cost == 0:
                            q.appendleft((x, y))
                            portal[matrix[x][y]] = (-1, -1)
                            portal.pop(matrix[x][y])
                        else:
                            q.append((x, y))
                            
        return dist[-1][-1] if dist[i][j] != sys.maxsize else -1
    