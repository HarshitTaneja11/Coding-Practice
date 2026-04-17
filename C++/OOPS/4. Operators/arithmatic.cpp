#include <iostream>

using namespace std;

int main()
{
    // int cups;
    // float pricePerCup, totalPrice, discountedPrice;
    // cout << "Enter the number of tea cups:" << endl;
    // cin >> cups;

    // cout << "Enter the price per cup:" << endl;
    // cin >> pricePerCup;

    // totalPrice = pricePerCup * cups;

    // if (totalPrice > 100)
    // {
    //     totalPrice = totalPrice - (5 * totalPrice) / 100;
    //     cout << "The total bill after 5 percent discount is Rupees " << totalPrice << endl;
    // }
    // else
    // {
    //     cout << "The total bill is Rupees " << totalPrice << endl;
    // }

    // int teabags;

    // cout << "Enter the number of teabags you have: ";
    // cin >> teabags;

    // if (teabags < 10)
    // {
    //     teabags = teabags + 5;
    // }

    // cout << "Your total bags are: " << teabags;

    int cups;

    cout << "Enter the number of cups you have: ";
    cin >> cups;

    if (cups >= 20)
    {
        cout << "You will get a GOLD badge";
    }

    else if (cups >= 10 && cups <= 20)
    {
        cout << "You will get a SILVER badge";
    }

    else
    {
        cout << "You will get NO badge";
    }
}