from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # if n == 1 and m == 1 and grid[0][0] == 0:
        #     return 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                # (i, j)是新鲜橘子，它周围都是空格子或者边界（这只是一种情况， 帮助提前跳出。实际上会有成片的新鲜橘子的情形，这里不讨论，放在末尾检测）
                elif grid[i][j] == 1:
                    flag = True
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < m and grid[x][y] != 0:
                            flag = False
                    if flag:
                        return -1 
                    
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
                    
            ans += 1
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
            
        if ans > 0:
            return ans - 1
        else:
            return 0
        