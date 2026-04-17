#include <iostream>
#include <string>

using namespace std;

int main()
{
    string response;

    while (true)
    {
        cout << "Do you want more tea?(type 'STOP to exit): ";
        getline(cin, response);

        if (response == "STOP") 
        {
            break;
        }
        

        cout << "Here is another cup of tea\n";
    }

    cout << "No more tea will be served";
    
}