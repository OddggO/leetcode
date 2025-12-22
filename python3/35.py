from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        m = (l + r) // 2
        while l <= r and nums[m] != target:
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
                
        if nums[m] == target:
            return m
        return r + 1 # target 在 nums[r] 后面
        