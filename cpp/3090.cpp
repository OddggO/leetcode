#include <iostream>
#include <string>
#include <map>
using namespace std;

class Solution {
public:
    int maximumLengthSubstring(string s) {
        int m[26] = {0};
        int ans = 0;
        int j = 0;
        for (int i = 0; i < s.size(); ++i) {
            int ii = s[i] - 'a';
            ++m[ii];
            while (j < i && m[ii] > 2) {
                --m[s[j] - 'a'];
                ++j;
            }
            ans = max(ans, i - j + 1);
        }
        return ans;
    }
};