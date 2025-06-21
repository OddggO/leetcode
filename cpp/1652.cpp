#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int len = code.size();
        vector<int> ans(len);
        int r = k > 0 ? k + 1 : len;
        k = abs(k);
        int s = accumulate(code.begin() + r - k, code.begin() + r, 0);
        for (int i = 0; i < len; ++i) {
            ans[i] = s;
            s += code[r % len] - code[(r - k) % len];
            ++r;
        }
        return ans;
    }
};