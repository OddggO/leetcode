class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x and y:
            i, j = x % 2, y % 2
            if i != j:
                ans += 1
            x //= 2
            y //= 2
        
        if not x:
            x = y
        while x:
            i = x % 2
            if i:
                ans += 1
            x //= 2
        return ans