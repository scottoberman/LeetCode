#include <vector>
#include <fstream>
#include <iostream>
using namespace std;


class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies)
    {
        int candiesSize = candies.size();
        vector<bool> canHaveMax;
        unsigned char maxKidCandy = 0;
        vector<int>::iterator it;
        vector<int>::iterator begin = candies.begin();
        vector<int>::iterator end = candies.end();
        int x;
        int candiesEndInt = candiesSize;
        for (x = 0 ; x != candiesEndInt; ++x)
        {
            if (candies[x] > maxKidCandy)
                maxKidCandy = candies[x];
        }

        for (x = 0; x != candiesEndInt; ++x)
        {
            bool canBeGreatest = false;
            if (candies[x] + extraCandies >= maxKidCandy)
                canBeGreatest = true;
            canHaveMax.emplace_back(canBeGreatest);
        }

        return canHaveMax;
    }

    void start()
    {
        vector<int> candy1;
        candy1.push_back(1);
        candy1.push_back(2);
        candy1.push_back(3);
        candy1.push_back(4);
        int extraCandies1 = 2;

        vector<int> candy2;
        candy2.push_back(3);
        candy2.push_back(6);
        candy2.push_back(5);
        candy2.push_back(9);
        int extraCandies2 = 3;

        kidsWithCandies(candy1, extraCandies1);
        kidsWithCandies(candy2, extraCandies2);


    }
};


int main()
{
    Solution sol;

    sol.start();
    
    return 0;
}