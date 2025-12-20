#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int numberOfSubstrings(string s) {
        int ans = 0, left = 0;
        unordered_map<char, int> cnt;
        for (auto c : s) {
            ++cnt[c];
            while (cnt.size() == 3){
                char out = s[left];
                --cnt[out];
                if (cnt[out] == 0) {
                    cnt.erase(out);
                }
                ++left;
            }
            ans += left;
        }
        return ans;
    }
};