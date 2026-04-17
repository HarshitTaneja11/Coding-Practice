#include <iostream>
#include <string>
#include <vector>

using namespace std;

// base/main/parent/orignal class

class Tea
{
protected:
    string teaname;
    int servings;

public:
    Tea(string name, int serve)
    {
        teaname = name;
        servings = serve;
        cout << "Tea constructor called " << teaname << endl;
    }

    virtual void brew()
    {
        cout << "Brewing: " << teaname << endl;
    }

    virtual void serve()
    {
        cout << "Serving " << teaname << endl;
    }

    virtual ~Tea()
    {
        cout << "Tea destructor called for " << teaname << endl;
    }
};

class GreenTea : public Tea
{
public:
    GreenTea(int serve) : Tea("Green Tea", 5)
    {
        cout << "Green Tea constuctor called" << endl;
    }

    void brew() override
    {
        cout << "Brewing " << teaname << "By steeping Green Tea leaves" << endl;
    }

    ~GreenTea()
    {
        cout << "Green Tea destructor called" << endl;
    }
};

class MasalaTea : public Tea
{
public:
    MasalaTea(int serve) : Tea("Masala Tea", 8)
    {
        cout << "Masala Tea constuctor called" << endl;
    }

    void brew() override final
    {
        cout << "Brewing " << teaname << endl;
    }

    ~MasalaTea()
    {
        cout << "Masala Tea destructor called" << endl;
    }
};

int main()
{
    GreenTea green;
    // MasalaTea masala;

    green.brew();
}