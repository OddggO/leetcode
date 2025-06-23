class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = vowel = 0
        for i, ch in enumerate(s):
            if ch in "aeiou":
                vowel += 1
            if i < k:
                ans = vowel
                continue
            if s[i - k] in "aeiou":
                vowel -= 1
            if ans < vowel:
                ans = vowel
        return ans