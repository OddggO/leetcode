#include <string>
using namespace std;

class Solution {
public:
    int minOperations(string s) {
        int n = s.size();
        int diff = 0;
        for (int i = 0; i < n; ++i)
        {
            if (i % 2 != s[i] - '0') 
                ++diff;
        }
        return min(diff, n - diff);
    }
};