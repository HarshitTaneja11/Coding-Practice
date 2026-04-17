// 1. Constructor Overloading
// 2. Function Overloading
#include <iostream>

using namespace std;

class Print
{
public:
    void show(int x)
    {
        cout << "Integer = " << x << endl;
    }

    void show(char ch)
    {
        cout << "Char = " << ch << endl;
    }
};

int main()
{
    Print p1, p2;
    p1.show(2);
    p2.show('H');
}