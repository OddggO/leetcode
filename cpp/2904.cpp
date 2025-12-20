#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int l = 0, r = 0;
        int n = s.size();
        string ans;
        int cnt = 0;
        while (r < n) {
            cnt += s[r] == '1' ? 1 : 0;
            while (cnt > k) {
                cnt -= s[l] == '1' ? 1 : 0;
                ++l;
            }
            while (s[l] == '0') {
                ++l;
            }
            if (cnt == k) { // 美丽字符串
                int len = r - l + 1;
                if (ans.size() == 0 || ans.size() > len) {  // 更短的美丽字符串
                    ans = s.substr(l, len);
                } else if (ans.size() == len) { // 判断哪个美丽字符串字典序更小
                    for(int i = 0; i < ans.size(); ++i) {
                        if (ans[i] > s[l + i]) {
                            ans = s.substr(l, len);
                            break;
                        }
                        if (ans[i] < s[l + i]) {
                            break;
                        }
                    }
                }
            }
            ++r;
        }
        return ans;
    }
};