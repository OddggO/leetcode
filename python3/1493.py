from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        j = 0
        n = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                n += 1
                if n == 2:
                    j += 1