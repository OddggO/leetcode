#include <iostream>
#include <vector>
#include <string>
using namespace std;


class Solution {
public:
    bool checkOnesSegment(string s) {
        int n = s.size();
        int l = 1;
        for (int i = 1; i < n; ++i) {
            if (s[i] != s[i - 1] && s[i] == '1')
                ++l;
        }
        
        return l <= 1 ? true : false;
    }
};

