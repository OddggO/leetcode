from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r = 0, 0
        s = sum(nums)
        n = len(nums)
        if s == x:
            return n
        ans, cnt = 0, s
        while r < n:
            while cnt > x:
                cnt -= nums[r]
                r -= 1