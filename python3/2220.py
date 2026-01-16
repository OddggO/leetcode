class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        x, y = start, goal
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