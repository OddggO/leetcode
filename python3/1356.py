from typing import List

class Solution:
    def countOne(self, num) -> int:
        res = 0
        while num:
            if num % 2:
                res += 1
            num //= 2
        return res
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr_one = [(self.countOne(num), num) for num in arr]
        arr_one_sorted = sorted(arr_one, key=lambda x: (x[0], x[1]))
        ans = [a[1] for a in arr_one_sorted]
        return ans
        