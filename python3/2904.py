class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l, r = 0, 0
        ans = ""
        cnt = 0
        n = len(s)
        while r < n:
            cnt += 1 if s[r] == '1' else 0
            while cnt > k:
                cnt -= 1 if s[l] == '1' else 0
                l += 1
            while l <= r and s[l] == '0':
                l += 1
            if cnt == k:
                n2 = r - l + 1
                if ans == "" or len(ans) > n2:
                    ans = s[l : r + 1]
                elif len(ans) == n2:
                    for i in range(n2):
                        if ans[i] > s[l + i]:
                            ans = s[l: r + 1]
                            break
                        if ans[i] < s[l + i]:
                            break
            r += 1
        return ans