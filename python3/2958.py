from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans, cur = 0, 0
        l, r = 0, 0
        n = len(nums)
        while r < n:
            cur += 1
            cnt[nums[r]] += 1
            while cnt[nums[r]] > k:
                cur -= 1
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    cnt.pop(nums[l])
                l += 1
            ans = max(ans, cur)
            r += 1
        return ans