class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        cur = blocks[:k].count('W')
        ans = cur
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                cur -= 1
            if blocks[i] == 'W':
                cur += 1
            if cur < ans:
                ans = cur
        return ans