#include <iostream>

using namespace std;

class Shape
{                            // abstract class
    virtual void draw() = 0; // pure virtual function
};

class circle : public Shape
{
public:
    void draw()
    {
        cout << "drawing a circle\n";
    }
};

int main()
{
    circle c1;
    c1.draw();
}