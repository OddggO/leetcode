class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cnt = sum(nums[:k])
        maxCnt = cnt
        for i in range(k, len(nums)):
            cnt = cnt - nums[i - k] + nums[i]
            if cnt > maxCnt:
                maxCnt = cnt
        return float(maxCnt) / k