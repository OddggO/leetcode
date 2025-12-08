#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        map<int, int> cnt;
        int ans = 0, cur = 0;
        int l = 0, r = 0;
        int len = nums.size();
        while (r < len) {
            ++cur;
            ++cnt[nums[r]];
            while (cnt[nums[r]] > k) {
                --cur;
                --cnt[nums[l]];
                if (cnt[nums[l]] == 0) {
                    cnt.erase(nums[l]);
                }
                ++l;
            }
            ans = max(ans, cur);
            ++r;
        }
        return ans;
    }
};