from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                i = j = mid
                break
            elif nums[mid] < target:
                i = mid
            else:
                j = mid
        if nums[mid] != target:
            return [-1, -1]
        while i > 0 and nums[i] == target:
            i -= 1
        while i < n - 1 and nums[i] == target:
            j += 1
        return [i, j]