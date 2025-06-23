#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int len = cardPoints.size();
        int cur = accumulate(cardPoints.begin() + len - k, cardPoints.end(), 0);
        int ans = cur;
        for (int i = 0; i < k; ++i) {
            cur = cur - cardPoints[len - k + i] + cardPoints[i];
            if (cur > ans) {
                ans = cur;
            }
        }
        return ans;
    }
};