#include <iostream>
#include <vector>

using namespace std;

class chai
{
public:
    string teaname;
    int servings;
    vector<string> ingredients;

    // chai() // Default Constructor
    // {
    //     teaname = "Unknown Tea";
    //     servings = 1;
    //     ingredients = {"Water", "Sugar", "TeaLeaves"};
    //     cout << "Default Constructor Called" << endl;
    // }

    chai(string name, int serve, vector<string> recipe) // Paramter Constructor
    {
        teaname = name;
        servings = serve;
        ingredients = recipe;
        cout << "Parameter Constructor Called" << endl;
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
};

int main()
{
    // chai defaultchai = chai("Green Tea", 5, {"Milk", "Sugar"});
    chai c1 = chai("Green Tea", 5, {"Milk", "Sugar"});
    c1.displaychaidetails();
    

    return 0;
}