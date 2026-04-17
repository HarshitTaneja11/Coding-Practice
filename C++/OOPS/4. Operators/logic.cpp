#include <iostream>

using namespace std;

int main()
{
    bool isStudent;
    cout << "Are you a student?(1 for YES and 0 for NO)";
    cin >> isStudent;

    int teacups;
    cout << "Hoe many cups of tea have you purchased?";
    cin >> teacups;

    if (isStudent == 1 || teacups > 15)
    {
        cout << "You are eligible for a discount";
    }
    else
    {
        cout << "You are NOT eligible for a discount";
    }

    return 0;
}