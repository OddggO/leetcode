class Solution:
    # def isZhiwei(self, x: int) -> bool:
    #     while x:
    #         if x % 2 != 1:
    #             return False
    #         x = x // 2
    #     return True
    # def smallestNumber(self, n: int) -> int:
    #     while not self.isZhiwei(n):
    #         n += 1
        
    #     return n
    
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1