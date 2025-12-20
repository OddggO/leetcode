class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        m = {}
        j = 0
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 1
            else:
                m[s[i]] += 1
            while j < i and m[s[i]] > 2:
                m[s[j]] -= 1
                j += 1
            ans = max(ans, i - j + 1)
        return ans