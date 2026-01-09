class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        while n and k:
            i, j = n % 2, k % 2
            if i == 0 and j == 1:
                return -1
            if i != j:
                ans += 1
            n = n >> 1
            k = k >> 1
        if k:
            return -1
        if n:
            while n:
                if n % 2:
                    ans += 1
                n = n >> 1
        return ans