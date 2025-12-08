#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        // 双指针+哈希表
        int left = 0, right = 0;
        map<int, int> cnt;
        int len = fruits.size();
        int ans = 0;
        while (right < len) {
            cnt[fruits[right]] += 1;
            while (cnt.size() > 2) {
                int out = fruits[left];
                cnt[out] -= 1;
                if (cnt[out] == 0) {
                    cnt.erase(out);
                }
                ++left;
            }
            ans = max(ans, right - left + 1);
            ++right;
        }
        return ans;
    }
};