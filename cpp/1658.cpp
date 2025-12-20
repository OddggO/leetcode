#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        s -= x;
        if (s < 0) {
            return -1;
        }
        int l = 0, r = 0;
        int ans = -1, cnt = 0;
        int len = nums.size();
        while (r < len) {
            cnt += nums[r];
            while (cnt > s) {
                cnt -= nums[l];
                ++l;
            }
            if (cnt == s) {
                ans = max(ans, r - l + 1);
            }
            ++r;
        }
        return ans == -1 ? -1 : len - ans;
    }
};