"""
解题思路：前缀和
计算数组总和total
遍历数组，记录当前位置前缀和cnt，
如果total == 2 * cnt + nums[i]，返回i，
遍历结束返回-1
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        cnt = 0
        for i in range(len(nums)):
            if (total == 2 * cnt + nums[i]):
                return i
            cnt += nums[i]
        return -1