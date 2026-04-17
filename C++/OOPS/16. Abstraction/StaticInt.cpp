#include <iostream>

using namespace std;

void fun()
{
    // int x = 0;
    static int x = 0; // x gets initialized ONCE during whole run time of the program
    cout << "x : " << x << endl;
    x++;
}

class A
{
public:
    int x;

    void incX()
    {
        x = x + 1;
    }
};

int main()
{
    fun();
    fun();
    fun();

    A obj1, obj2;
    obj1.x = 100;
    obj2.x = 200;
    cout << obj1.x << endl;
    obj1.incX();
    cout << obj1.x << endl;

    cout << obj2.x << endl;
    obj2.incX();
    cout << obj2.x << endl;
}