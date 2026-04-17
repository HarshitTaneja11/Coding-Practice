#include <iostream>
#include <vector>

using namespace std;

class chai
{
public:
    string *teaname;
    int servings;
    vector<string> ingredients;

    chai(string name, int serve, vector<string> ingredient)
    {
        *teaname = name;
        servings = serve;
        ingredients = ingredient;
        cout << "Param Constructor Called" << endl;
    }

    void displaychaidetails()
    {
        cout << "Tea name: " << teaname << endl;
        cout << "Servings: " << servings << endl;
        cout << "ingredients: ";
        for (string ingredient : ingredients)
        {
            cout << ingredient << " ";
        }

        cout << endl;
    }

    ~chai()
    {
        delete teaname;
        cout << " destructor called";
    }
};

int main()
{
    chai LemonTea("Lemon Tea", 3, {"Water", "Lemon", "Honey"});

    LemonTea.displaychaidetails();

    chai copy = LemonTea;
    copy.displaychaidetails();

    return 0;
}