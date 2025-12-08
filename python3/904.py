from typing import List

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         l, r = 0, 1 # 左、右指针
#         ans = 0
#         basket1, basket2 = fruits[l], -1
#         n = len(fruits)
#         while r < n:
#             if fruits[r] == basket1:
#                 pass
#             elif basket2 == -1:
#                 basket2 = fruits[r]
#             elif fruits[r] != basket2:
#                 ans = max(ans, r - l)
#                 t = r - 2 # 按照初始化和这个if else的逻辑，r < 2的情况不会出现，所以不必判断
#                 while fruits[t] == fruits[r - 1]:
#                     t -= 1
#                 l = t + 1
#                 basket1 = fruits[l]
#                 basket2 = fruits[r]
#             print(l, r, ans)
#             r += 1
#         return max(ans, r - l)

# 哈希表解法
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0 # 左、右指针
        ans = 0
        m = defaultdict(int)
        n = len(fruits)
        while r < n:
            m[fruits[r]] += 1
            while len(m) > 2:
                out = fruits[l]
                m[out] -= 1
                if m[out] == 0:
                    m.pop(out)
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
        