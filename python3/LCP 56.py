from typing import List
import sys
from collections import deque

class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        n, m = len(matrix), len(matrix[0])
        dist = [[sys.maxsize] * m for _ in range(n)]
        dist[start[0]][start[1]] = 0
        q = deque()
        q.append((start[0], start[1]))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        directions_flag = ['>', '<', 'v', '^']
        while q:
            i, j = q.popleft()
            if i == end[0] and j == end[1]:
                return dist[i][j]
            d = matrix[i][j]
            for p, (dx, dy) in enumerate(directions):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    cost = 0
                    if directions_flag[p] != d:
                        cost = 1
                    if cost + dist[i][j] < dist[x][y]:
                        dist[x][y] = cost + dist[i][j]
                        if cost == 0:
                            q.appendleft((x, y))
                        else:
                            q.append((x, y))
                        # print((i, j), (x, y), cost, dist[x][y], directions_flag[p])
                        
        return -1
    
if __name__ == "__main__":
    matrix = [">>v","v^<","<><"]
    start = [0,1]
    end = [2,0]
    slt = Solution()
    ret = slt.conveyorBelt(matrix, start, end)
    print(ret)
    