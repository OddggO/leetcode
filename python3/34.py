from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        l, r = 0, n - 1
        mid = (l + r) // 2
        while l < r and nums[mid] != target:
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2
                
        if l >= r: # 如果while退出时，分为1) l = r = mid；2）l = r + 1，mid = (r + 1 + r) // 2 = r (只有两个元素造成mid = -1时， 刚好符合要求)
            if nums[mid] == target:
                return [mid, mid]
            else:
                return [-1, -1]
        
        l = mid
        while l >= 0 and nums[l] == target:
            l -= 1
            
        r = mid
        while r < n and nums[r] == target:
            r += 1
        
        return [l + 1, r - 1]