from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = []
        q.append(entrance)
        m, n = len(maze), len(maze[0])
        # flag = [[False for _ in range(m)] for _ in range(n)]
        flag = [[False] * n for _ in range(m)]
        flag[entrance[0]][entrance[1]] = True
        ans = 1
        while q:
            p = q
            q = []
            for e in p:
                i, j = e[0], e[1]
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < m and 0 <= y < n and flag[x][y] != True and maze[x][y] == ".":
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            return ans
                        flag[x][y] = True
                        q.append([x, y])
            ans += 1

        return -1
