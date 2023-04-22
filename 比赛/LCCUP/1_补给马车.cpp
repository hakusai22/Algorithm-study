/*
 * @Author: hakusai
 * @Date: 2023-04-22 17:42:21
 * @LastEditTime: 2023-04-22 21:10:51
 */
#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> supplyWagon(vector<int> &a)
    {
        int n = (int)a.size(), m = n / 2;
        while (n > m)
        {
            int pos = 0, minn = 1e9;
            for (int i = 0; i < n - 1; i++)
            {
                if (a[i] + a[i + 1] < minn)
                {
                    minn = a[i] + a[i + 1];
                    pos = i;
                }
            }
            a[pos] += a[pos + 1];
            for (int i = pos + 1; i < n - 1; i++)
                a[i] = a[i + 1];
            a.pop_back();
            --n;
        }
        return a;
    }
};

int main()
{
    Solution supplyWagon;
    vector<int> nums;
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(4);
    nums.push_back(5);
    vector<int> result = supplyWagon.supplyWagon(nums);
    for (unsigned int i = 0; i < result.size(); ++i)
    {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
