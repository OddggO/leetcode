class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        num_map = {} # 当前窗口各元素出现的次数
        cnt = 0 # 当前窗口数字总和
        """计算第一个窗口的不系统元素个数和窗口数字总和"""
        for i in range(0, k):
            if nums[i] not in num_map:
                num_map[nums[i]] = 1
            else:
                num_map[nums[i]] += 1
            cnt += nums[i]
        ans = cnt if len(num_map) >= m else 0 # 结果
        """移动窗口：cnt变化、字段变化、cur变化、结果变化"""
        for i in range(k, len(nums)):
            cnt -= nums[i - k]
            if num_map[nums[i - k]] == 1:
                num_map.pop(nums[i - k])
            else:
                num_map[nums[i - k]] -= 1
            if nums[i] not in num_map:
                num_map[nums[i]] = 1
            else:
                num_map[nums[i]] += 1
            cnt += nums[i]
            if len(num_map) >= m and cnt > ans:
                ans = cnt
        return ans
            