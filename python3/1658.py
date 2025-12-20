from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        s -= x
        if s < 0:
            return -1
        l, r = 0, 0
        ans, cnt = -1, 0
        n = len(nums)
        while r < n:
            cnt += nums[r]
            while cnt > s:
                cnt -= nums[l]
                l += 1
            if cnt == s:
                ans = max(ans, r - l + 1)
            r += 1
        return n - ans if ans != -1 else -1