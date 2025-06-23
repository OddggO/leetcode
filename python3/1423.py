from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        cur = sum(cardPoints[length - k : length])
        ans = cur
        for i in range(0, k):
            cur = cur - cardPoints[length - k + i] + cardPoints[i]
            if cur > ans:
                ans = cur
        return ans