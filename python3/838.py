class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        cur = 0
        l, r = 0, -1
        while n:
            if n % 2:
                if r == -1:
                    r = l
                else:
                    cur = l - r + 1
                    if cur > ans:
                        ans = cur
                    r = l
            l += 1
            n //= 2
        return ans
    