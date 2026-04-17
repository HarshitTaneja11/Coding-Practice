#include <iostream>
#include <string>

using namespace std;

int main()
{
    auto chai = [](int cups)  // ye topic aage aayega in libraries 
    {
        cout << "Preparing " << cups << " cups of tea" << endl;
    };

    chai(4);
}