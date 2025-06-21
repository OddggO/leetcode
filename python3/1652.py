from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        r = k + 1 if k > 0 else n
        k = abs(k)
        s = sum(code[r - k : r])
        for i in range(n):
            ans[i] = s
            s += code[r % n] - code[(r - k) %n]
            r += 1
        return ans