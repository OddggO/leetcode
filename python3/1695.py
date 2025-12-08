from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        ans, cur = 0, 0
        l, r = 0, 0
        n = len(nums)
        while r < n:
            cur += nums[r]
            if nums[r] not in s:
                s.add(nums[r])
            else:
                while nums[l] != nums[r]:
                    cur -= nums[l]
                    s.remove(nums[l])
                    l += 1
                cur -= nums[l]
                # s.remove(nums[l])
                l += 1
            ans = max(ans, cur)
            r += 1
        return ans