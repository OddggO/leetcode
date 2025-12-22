from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n - 1
        m = (l + r) // 2
        while l <= r and letters[m] != target:
            print(m, letters[m])
            if letters[m] < target:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
            
        # if l <= r:
        #     return letters[m + 1] if m + 1 < n else letters[0]
        # else:
        #     return letters[r + 1] if r + 1 < n and letters[r + 1] > target else letters[0]
            # return letters[r] if r >= 0 else letters[0]
        if letters[m] == target:
            while m < n and letters[m] == target:
                m += 1
            return letters[m] if m < n else letters[0]
        else:
            return letters[r + 1] if r + 1 < n and letters[r + 1] > target else letters[0]
            