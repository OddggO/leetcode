from typing import List
from queue import Queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, _ = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n == 1:
            return 1
        flag = [[False] * n for _ in range(n)]
        flag[0][0] = True
        q = Queue()
        q.put((0, 0, 1))
        while not q.empty():
            node = q.get()
            i, j, v = node[0], node[1], node[2]
            if i == j == n - 1:
                return v
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), \
                (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1):
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and not flag[x][y]:
                        flag[x][y] = True
                        q.put((x, y, v + 1))
                        
        return -1
        