from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        ans, cnt = 0, 0
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                cnt += 1
            while cnt > k:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans