#include <iostream>
#include <string>

using namespace std;

int main()
{
    string TeaTypes[3] = {"Green Tea", "Black Tea", "Oolong Tea"};

    for (int  i = 0; i < 3; i++)
    {
        cout << "Brewing " << TeaTypes[i] << "..." << endl;
        for (int j = 1; j <= 3; j++)
        {
            cout << "Brewed " << j << " Cup of " << TeaTypes[i] << endl;
        }
        
    }
    
}