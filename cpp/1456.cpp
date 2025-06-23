#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution {
    inline bool isVowel(const char& ch) {
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            return true;
        return false;
    }
public:
    int maxVowels(string s, int k) {
        int len = s.size();
        int ans = 0, vowel = 0;
        for(int i = 0; i < len; ++i) {
            if (isVowel(s[i])) {
                ++vowel;
            }
            if (i < k) {
                ans = vowel;
                continue;
            }
            if (isVowel(s[i - k])) {
                --vowel;
            }
            if (ans < vowel) {
                ans = vowel;
            }
        }
        return ans;
    }
};