#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    vector<int> a = {1, 2, 3};
    vector<int> b = a;
    b[0] = 10;
    for (int i = 0; i < a.size(); ++i)
    {
        cout << a[i] << " " << b[i] << endl;
    }
}
