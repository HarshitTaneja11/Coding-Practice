#include <iostream>

using namespace std;

int totalchai(int chai[], int size)
{
    int total = 0;
    for (int i = 0; i < size; i++)
    {
        total += chai[i];
    }
    return total;
}

int main(){
    int chaiserved[7] = {12,34,46,23,57,97,23};
    int total = totalchai(chaiserved, 7);
    cout << total;
}