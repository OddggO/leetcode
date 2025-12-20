#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int ans = 0, cnt = 0;
        int i = 0, j = 0;
        int len = s.size();
        while (i < len) {
            cnt += abs(s[i] - t[i]);
            while (j < i && cnt > maxCost) {
                cnt -= abs(s[j] - t[j]);
                ++j;
            }
            if (i == j && cnt > maxCost) {
                ans = max(ans, 0);
            } else {
                ans = max(ans, i - j + 1);
            }
            ++i;
        }
        return ans;
    }
};