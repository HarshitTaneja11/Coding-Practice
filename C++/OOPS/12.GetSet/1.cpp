#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Chai
{
private:
    string teaname;
    int servings;
    vector<string> ingredients;

public:
    Chai()
    {
        teaname = "Unknown Tea";
        servings = 1;
        ingredients = {
            "Water",
            "Tea leaves",
        };
    }

    Chai(string name, int serve, vector<string> ingr)
    {
        teaname = name;
        servings = serve;
        ingredients = ingr;
    }

    // getter
    string getteaname()
    {
        return teaname;
    }

    // setter
    void setteaname(string name)
    {
        teaname = name;
    }

    int getservings()
    {
        return servings;
    }

    void setservings(int serve)
    {
        servings = serve;
    }

    void display()
    {
        cout << "Tea Name: " << teaname << endl;
        cout << "Servings: " << servings << endl;
        cout << "Ingredients: ";
        for (string ingredients : ingredients)
        {
            cout << ingredients << " ";
        }
        cout << endl;
    }
};

int main()
{
    Chai chai;
    chai.setteaname("Green Tea");
    chai.display();
}