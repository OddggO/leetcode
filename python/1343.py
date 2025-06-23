class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        threshold *= k
        cnt = sum(arr[:k])
        ans = 1 if cnt >= threshold else 0
        for i in range(k, len(arr)):
            cnt = cnt - arr[i - k] + arr[i]
            if cnt >= threshold:
                ans += 1
        return ans