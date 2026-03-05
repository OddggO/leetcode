#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    string s = "010101";
    for (int i = 0; i < s.size(); ++i)
    {
        // printf("%c %c %d\n", s[i], *(s.data() + i), atoi(s.data() + i));
        printf("%c %c %d\n", s[i], *(s.data() + i), s[i] - '0');
    }
    return 0;
}
