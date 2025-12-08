from collections import defaultdict

class Solution:
    # def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    #     l, r = 0, 0
    #     ans, t, f = 0, 0, 0
    #     n = len(answerKey)
    #     while r < n:
    #         if answerKey[r] == 'T':
    #             t += 1
    #         else:
    #             f += 1
    #         while min(t, f) > k:
    #             if answerKey[l] == 'T':
    #                 t -= 1
    #             else:
    #                 f -= 1
    #             l += 1
    #         ans = max(ans, r - l + 1)
    #         r += 1
    #     return ans
    
    # method 2: 字典
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, r = 0, 0
        ans = 0
        cnt = defaultdict(int)
        n = len(answerKey)
        while r < n:
            cnt[answerKey[r]] += 1
            while cnt['T'] > k and cnt['F'] > k:
                cnt[answerKey[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans