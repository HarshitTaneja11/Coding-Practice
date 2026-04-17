#include <iostream>
#include <vector>

using namespace std;

// class is orignal form

class Chai // Class (Orignal)
{
public:
    string teaname;
    int servings;
    vector<string> ingredients;

    // member function

    void displaychaidetails();  // defining function inside the class
    // {
    //     cout << "Tea name: " << teaname << endl;
    //     cout << "Servings: " << servings << endl;
    //     cout << "ingredients: ";
    //     for (string ingredient : ingredients)
    //     {
    //         cout << ingredient << " ";
    //     }

    //     cout << endl;
    // }
};

void Chai ::displaychaidetails() // definingfunction outside the class using scope resolution operator
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

int main()
{
    Chai c1; // Object (copy of class)

    c1.teaname = "Masala Tea";
    c1.servings = 10;
    c1.ingredients = {"Milk", "Water", "Patti", "Masale"};

    c1.displaychaidetails();
    cout << endl;

    Chai c2; // Object (copy of class)

    c2.teaname = "Adrak Chai";
    c2.servings = 2;
    c2.ingredients = {"Milk", "Water", "Patti", "Adrak"};

    c2.displaychaidetails();

    return 0;
}