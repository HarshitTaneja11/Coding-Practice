#include <iostream>
#include <string>

using namespace std;

int main()
{
//     string tea;

//     cout << "Enter your tea order: ";
//     getline (cin, tea);

//     if (tea == "Green Tea")     
//     {
//         cout << "Order Confirmed!!";
//     }

    int hour;

    cout << "Enter the time(24hr format): ";
    cin >> hour;

    if (hour >= 8 && hour <= 18)
    {
        cout << "Shop is open";
    }
    else
    cout << "Shop is closed";



    
}