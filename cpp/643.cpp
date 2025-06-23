#include <iostream>
#include <vector>
#include <string>
#include <numeric>
using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int cnt = accumulate(nums.begin(), nums.begin() + k, 0);
        int maxCnt = cnt;
        for(int i = k; i < nums.size(); ++i) {
            cnt = cnt - nums[i - k] + nums[i];
            if (cnt > maxCnt) {
                maxCnt = cnt;
            }
        }
        return double(maxCnt) / k;
    }
};