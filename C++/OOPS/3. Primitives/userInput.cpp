#include <iostream>
#include <string>

using namespace std;

int main()
{
    string usertea;

    int qty;

    cout << "Which tea would you like to order?" << endl;

    getline(cin, usertea);

    cout << "How mant cups of " << usertea << "would you like to have?\n";
    cin >> qty;

    cout << "You have ordered " << qty << " cups of " << usertea << " tea .\n";
}