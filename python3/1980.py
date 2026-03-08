from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in n:
            s = ""
            for j in range(2):
                if j:
                    s += "1"
                else:
                    s += "0"