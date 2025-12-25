from typing import List
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        heights = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    
        # if not q or len(q) == 0 or len(q) == n * m:
        #     return -1
        h = 1
        while q:
            for _ in range(len(q)): # 记录当前这一层有多少元素，这样可以避免复制队列
                i, j = q.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and isWater[x][y] == 0:
                        isWater[x][y] = 1
                        heights[x][y] = h
                        q.append((x, y))
            h += 1
        return heights