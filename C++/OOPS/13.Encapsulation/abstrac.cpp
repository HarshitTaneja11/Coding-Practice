#include <iostream>
#include <string>

using namespace std;

class Tea
{
public:
    virtual void prepareIngredients() = 0;
    virtual void brew() = 0;
    virtual void serve() = 0;

    void maketea()
    {
        prepareIngredients();
        brew();
        serve();
    }
};

class GreenTea : public Tea
{
public:
    void prepareIngredients() override
    {
        cout << "Green leaves and water is ready" << endl;
    }
    void brew() override
    {
        cout << "Tea brewed" << endl;
    }
    void serve() override
    {
        cout << "Tea is served" << endl;
    }
};

class MasalTea : public Tea
{
public:
    void prepareIngredients() override
    {
        cout << "Masala and water is ready" << endl;
    }
    void brew() override
    {
        cout << "Masala Tea brewed" << endl;
    }
    void serve() override
    {
        cout << "Masala Tea is served" << endl;
    }
};

int main()
{
    GreenTea greentea;
    MasalTea masalatea;

    greentea.maketea();
    masalatea.maketea();

    return 0;
}