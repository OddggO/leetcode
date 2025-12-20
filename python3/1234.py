from collections import defaultdict
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1
        print(cnt)
        n = len(s) // 4
        print(n)
        cnt2 = defaultdict(int)
        for ch in list(cnt.keys()):
            if cnt[ch] > n:
                cnt[ch] -= n
                cnt2[ch] = 0
            else:
                cnt.pop(ch)
        print(cnt)
        if len(cnt) == 0:
            return 0
        def isBalancedString():
            for ch in cnt:
                if cnt2[ch] < cnt[ch]:
                    return False
            return True
        l, r = 0, 0
        ans = 4 * n
        while r < len(s):
            # 加入元素
            if s[r] in cnt:
                cnt2[s[r]] += 1
            # 当前是否是平衡字符串
            if isBalancedString():
                # 去除左边多余的元素
                while l < r and isBalancedString():
                    if s[l] in cnt:
                        cnt2[s[l]] -= 1
                    l += 1
                if not isBalancedString():
                    l -= 1
                    if s[l] in cnt:
                        cnt2[s[l]] += 1
                # 更新答案
                ans = min(ans, r - l + 1)
                print(l, r, ans)
                # 找到下一个关键点
                while l < r and s[l] in cnt:
                    cnt2[s[l]] -= 1
                    l += 1
                # if l == r:
                #     print(cnt, r, ans)
                #     return sum([cnt[k] for k in cnt])
                while l < r and s[l] not in cnt:
                    l += 1
            r += 1
        return ans