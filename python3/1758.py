class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        s0 = ['0' if i % 2 else '1' for i in range(n)]
        a0= 0
        for i in range(n):
            if s[i] != s0[i]:
                a0 += 1
        return min(a0, n - a0)
    # def minOperations(self, s: str) -> int:
    #     n = len(s)
    #     s0 = ['0' if i % 2 else '1' for i in range(n)]
    #     s1 = ['1' if i % 2 else '0' for i in range(n)]
    #     a0, a1 = 0, 0
    #     for i in range(n):
    #         if s[i] != s0[i]:
    #             a0 += 1
    #         if s[i] != s1[i]:
    #             a1 += 1
    #     return a0 if a0 < a1 else a1
    