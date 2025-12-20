class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        i, j = 0, 0
        cnt = 0
        while i < len(s):
            cnt += abs(ord(s[i]) - ord(t[i]))
            while j < i and cnt > maxCost:
                cnt -= abs(ord(s[j]) - ord(t[j]))
                j += 1
            if i == j and cnt > maxCost:
                ans = max(ans, 0)
            else:
                ans = max(ans, i - j + 1)
            i += 1
        return ans