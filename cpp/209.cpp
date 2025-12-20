#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        if (s - target < 0) {
            return 0;
        }
        sort(nums.begin(), nums.end());
        int l = 0, r = 0;
        int len = nums.size();
        int ans = len, cnt = s;
        while (r < len) {
            cnt += nums[r];
            if (cnt < target) {
                ++r; 
                continue;
            }
            while (cnt >= target) {
                cnt -= nums[l];
                --l;
            }
            ans = min(ans, r - l + 2);
            ++r;
        }
        return ans;
    }
};