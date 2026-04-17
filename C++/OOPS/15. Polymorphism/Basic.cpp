// Polymorphism is when object of a class behaves differently depending on the context in which it is used
#include <iostream>

using namespace std;

class student
{
public:
    string name;

    student()
    {
        cout << "Non-Parameterized constructor called" << endl;
    }

    student(string n)
    {
        this->name = n;
        cout << "Parameterized Constructor Called" << endl;
    }
};

int main()
{
    student s1("Harshit Taneja");
    student s2;
}