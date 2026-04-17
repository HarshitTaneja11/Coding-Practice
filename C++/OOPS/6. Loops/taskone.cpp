#include <iostream>
#include <string>

using namespace std;

int main()
{
    int teacup;

    cout << "How many cups of tea would you like to have?";
    cin >> teacup;

    while (teacup > 0)
    {
        cout << "Serving a cup of tea\n"
             << teacup << " Remaining" << endl;
        teacup = teacup - 1;
    }

    cout << "All cups of tea have been served, Enjoy :)";

    return 0;
}