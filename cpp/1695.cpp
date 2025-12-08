#include <iostream>
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        set<int> s;
        int ans = 0, cur = 0;
        int l = 0, r = 0;
        int len = nums.size();
        while (r < len) {
            cur += nums[r];
            if (s.find(nums[r]) == s.end()) {
                s.insert(nums[r]);
            } else {
                while (nums[l] != nums[r]) {
                    cur -= nums[l];
                    s.erase(nums[l]);
                    ++l;
                }
                cur -= nums[l];
                // s.erase(nums[l]);
                ++l;
            }
            ans = max(ans, cur);
            ++r;
        }
        return ans;
    }
};