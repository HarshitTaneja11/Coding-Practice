#include <iostream>
#include <string>
#include <vector>

using namespace std;

class chai
{

private:
    string teaname;
    int serving;

public:
    chai(string name, int serve) : teaname(name), serving(serve) {}

    void display()
    {
        cout << "Teaname: " << teaname << endl;
    }

    friend bool compare(const chai &chai1, const chai &chai2);
};


bool compare(const chai &chai1, const chai &chai2){
    return chai1.serving > chai2.serving;
}

int main()
{
    chai masalachai("Masala Chai", 14);
    chai gingertea("Ginger Tea", 5);

    gingertea.display();
    masalachai.display();

    if (compare(masalachai, gingertea)) 
    {
        cout << "Masala chai has MORE servings" << endl;
    }
    else
    cout << "Masala chai has LESS servings" << endl;
    
    
}