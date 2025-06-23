from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = [0, 0]
        ans = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            s[g] += c
            left = i - minutes + 1
            if left < 0:
                continue
            if s[1] > ans:
                ans = s[1]
            if grumpy[left] == 1:
                s[1] -= customers[left]
        return s[0] + ans