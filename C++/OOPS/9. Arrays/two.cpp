#include <iostream>

using namespace std;

int *preparechaiorder(int cups)
{
    int *orders = new int[cups];
    for (int i = 0; i < cups; i++)
    {
        orders[i] = (i + 1) * 10;
    }
    return orders;
}

// int totalchai(int chai[], int size)
// {
//     int total = 0;
//     for (int i = 0; i < size; i++)
//     {
//         total += chai[i];
//     }
//     return total;
// }

int main()
{
    int cups = 5;
    int *chaiorder = preparechaiorder(cups);

    for (int i = 0; i < cups; i++)
    {
        cout << "Cup: " << i + 1 << " has " << chaiorder[i] << "ml" << endl;
    }

    delete[] chaiorder;
}