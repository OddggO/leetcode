from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        cnt = {}
        cur = 0
        ans = 0
        for i in range(length):
            # 添加当前端点
            cur += nums[i]
            if nums[i] not in cnt: # 默认的字典结构有keyerror，即建不存在时访问会报错，可以用from collections import defaultdict代替
                cnt[nums[i]] = 1
            else:
                cnt[nums[i]] += 1
            
            # 窗口长度不足k，不更新和滑动左端点
            left = i - k + 1
            if left < 0:
                continue
            
            # 更新答案
            if cur > ans and len(cnt) == k:
                ans = cur
                
            # 离开左端点
            cur -= nums[left]
            if cnt[nums[left]] == 1:
                cnt.pop(nums[left])
            else:
                cnt[nums[left]] -= 1
        return ans
            