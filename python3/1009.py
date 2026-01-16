class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        order = 1
        while n:
            if n % 2 == 0:
                ans |= order
            order <<= 1
            n //= 2
        return ans