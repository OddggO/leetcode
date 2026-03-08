#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans = nums; // 拷贝
        ans.resize(nums.size() * 2);
        for (int i = n; i < 2 * n; ++i) {
            ans[i] = nums[i - n];
        }
        return ans;
    }
};