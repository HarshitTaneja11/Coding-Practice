/*
1. Function Overriding - Parent and child both contain same function with different implementation.
The parent class function is said to be overridden.

2. Virtual Functions- A virtual function is a member function that you expect
to be redefined in member(child) class.
*/
#include <iostream>

using namespace std;

// class Parent
// {
// public:
//     void show()
//     {
//         cout << "Parent Class\n";
//     }
// };

// class child : public Parent
// {
// public:
//     void show()
//     {
//         cout << "Child Class\n";
//     }
// };

class Parent
{
public:
    virtual void show()
    {
        cout << "Parent Class\n";
    }
};

class child : public Parent
{
public:
    void show() // The virtual function is redined in the child class.
    {
        cout << "Child Class\n";
    }
};

int main()
{
    child c1;
    c1.show();
    Parent p1;
    p1.show();
}