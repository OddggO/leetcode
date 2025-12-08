#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, r = 0;
        int ans = 0, cnt = 0;
        int len = nums.size();
        while (r < len) {
            if (!nums[r]) {
                ++cnt;
            }
            while (cnt > k) {
                if (!nums[l]) {
                    --cnt;
                }
                ++l;
            }
            ans = max(ans, r - l + 1);
            ++r;
        }
        return ans;
    }
};