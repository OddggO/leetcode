#include <iostream>
#include <vector>
#include <string>
#include <numeric>
using namespace std;

class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        threshold *= k;
        int cnt = accumulate(arr.begin(), arr.begin() + k, 0);
        int ans = cnt >= threshold ? 1 : 0;
        for(int i = k; i < arr.size(); ++i) {
            cnt = cnt - arr[i - k] + arr[i];
            if (cnt >= threshold) {
                ++ans;
            }
        }
        return ans;
    }
};