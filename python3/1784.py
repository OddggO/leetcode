class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        l = 1
        for i in range(1, n):
            if s[i] != s[i - 1] and s[i] == '1':
                l += 1

        return l <= 1
