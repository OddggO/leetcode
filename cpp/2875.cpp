#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int minSizeSubarray(vector<int>& nums, int target) {
        int l = 0, r = 0;
        int total = accumulate(nums.begin(), nums.end(), 0);
        int len = nums.size();
        int ans = INT_MAX, cnt = 0, rem = target % total;
        while (r < len * 2) {
            cnt += nums[r % len];
            while (cnt > rem) {
                cnt -= nums[l % len];
                ++l;
            }
            if (cnt == rem) {
                ans = min(ans, r - l + 1);
            }
            ++r;
        }
        return ans == INT_MAX? -1 : ans + target / total * len;
    }
};