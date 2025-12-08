from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        l, r = 0, 0
        n = len(nums)
        ans, cnt = n + 1, 0
        s = sum(nums)
        ans0 = 0
        if target > s:
            ans0 = (target // s) * n
            target = target % s
        while r < n:
            cnt += nums[r]
            while cnt > target:
                cnt -= nums[l]
                l += 1
            if cnt == target:
                ans = min(ans, r - l + 1)
            r += 1
        return ans0 + ans if ans != n + 1 else -1
        