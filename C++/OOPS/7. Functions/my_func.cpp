#include <iostream>
#include <string>

using namespace std;

void pourChai(int & chaicups)
{
    chaicups = chaicups + 5;
    cout << "Poured " << chaicups << " cups" << endl;
}

int main()
{
    int chaicups = 2;
    pourChai(chaicups);
    cout << "Total cups are " << chaicups << endl;
}