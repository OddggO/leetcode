#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int l = 0, r = 0;
        int ans = 0, t = 0, f = 0;
        int len = answerKey.size();
        while (r < len) {
            if (answerKey[r] == 'T') {
                ++t;
            } else {
                ++f;
            }
            while (min(t, f) > k) {
                if (answerKey[l] == 'T') {
                    --t;
                } else {
                    --f;
                }
                ++l;
            }
            ans = max(ans, r - l + 1);
            ++r;
        }
        return ans;
    }
};