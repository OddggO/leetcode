from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        m = (l + r) // 2
        while l <= r and nums[m] != target:
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
                
        # if l <= r:
        #     if nums[m] == target:
        #         return m
        #     else:
        #         return -1
        # else:
        #     # return -1
        #     pass 
        # 不需要考虑所有循环出口条件，利用递归思想思考循环出口：
        # 循环条件有nums[m] != target，m是l和r的均值向下取整，因此target在当前[l, r]区间之外，一定是错误的，
        # 由于l <= r，因此不需要在循环外考虑nums[m] == target
        return m if l <= r else -1