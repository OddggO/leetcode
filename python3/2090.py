class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        radius = 2 * k + 1
        if len(nums) < radius:
            return [-1] * len(nums)
        avg = [-1] * k
        cnt = sum(nums[:k])
        for i in range(k, len(nums)): 
            cnt += nums[i]
            if i < 2 * k:
                continue
            avg.append(cnt // radius)
            cnt -= nums[i - 2 * k]
        avg.extend([-1] * k)
        return avg
            