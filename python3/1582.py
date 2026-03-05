
# from ast import List
from typing import List

class Solution:
    def slt0(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows = [0] * n
        cols = [0] * m
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1

        ans = 0
        for i in range(n):
            for j in range(m):
                # if rows[i] == 1 and cols[j] == 1:
                if rows[i] == 1 and cols[j] == 1 and mat[i][j] == 1:
                    ans += 1

        return ans
    
    def slt1(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows = [sum(row) for row in mat]
        cols = [sum([mat[i][j] for i in range(n)]) for j in range(m)]

        ans = 0
        for i in range(n):
            for j in range(m):
                # if rows[i] == 1 and cols[j] == 1:
                if rows[i] == 1 and cols[j] == 1 and mat[i][j] == 1:
                    ans += 1

        return ans

    def numSpecial(self, mat: List[List[int]]) -> int:
        # return self.slt0(mat)
        return self.slt1(mat)