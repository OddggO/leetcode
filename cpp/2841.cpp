#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    long long maxSum(vector<int>& nums, int m, int k) {
        long long cur = 0; // 当前窗口总和
        long long ans = 0; // 最优解
        map<int, int> cnt; // 字典，记录窗口内每个元素出现的次数
        int len = nums.size();
        for(int i = 0; i < len; ++i) {
            // 窗口增加右端点
            cur += nums[i];
            ++cnt[nums[i]];
            // 确认窗口左端点的位置
            int left = i - k + 1;
            if (left < 0) { // 不是完整的窗口、继续延长窗口
                continue;
            }
            // 更新答案
            if (cnt.size() >= m && cur > ans) {
                ans = cur;
            }
            // 窗口离开左端点
            cur -= nums[left];
            if(--cnt[nums[left]] == 0) {
                cnt.erase(nums[left]);
            }
        }
        return ans;
    }
};