class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        n = 1
        while num:
            if num % 2 == 0:
                ans |= n
            n <<= 1
            num //= 2
        return ans