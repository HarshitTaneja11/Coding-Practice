#include <iostream>

using namespace std;

class Marks
{
    int intmark;
    int extmark;

public:
    Marks()
    {
        intmark = 0;
        extmark = 0;
    }

    Marks(int im, int em)
    {
        intmark = im;
        extmark = em;
    }

    void display()
    {
        cout << intmark << endl
             << extmark << endl;
    }

    Marks operator+(Marks m)  // '+' operator Overloading
    {
        Marks temp;
        temp.intmark = intmark + m.intmark;
        temp.extmark = extmark + m.extmark;
        return temp;
    }

    Marks operator-(Marks m)  // '-' operator overloading
    {
        Marks temp;
        temp.intmark = intmark - m.intmark;
        temp.extmark = extmark - m.extmark;
        return temp;
    }

};

int main()
{
    Marks m1(10, 20), m2(30, 40);

    Marks m3 = m1 + m2;

    m3.display();

    m3 = m1 - m2;

    m3.display();

    return 0;
}

class marks
{
    int mark;

public:
    marks()
    {
        mark = 0;
    }
    marks(int m)
    {
        mark = m;
    }

    void set_marks()
    {
        cout << " your marks are : " << mark << endl;
    }

    void operator+=(int bonus)
    {
        mark = mark + bonus;
    }

    friend void operator-=(marks &currentobj, int reduce);
};

void operator-=(marks &currentobj, int reduce)
{
    currentobj.mark -= reduce;
}

int main() {

    marks htmark(92);
    htmark.set_marks();

    htmark += 2;
    htmark.set_marks();

}

class marks
{
    int subjects[3];

public:
    marks(int a, int b, int c)
    {
        subjects[0] = a;
        subjects[1] = b;
        subjects[2] = c;
    }

    int operator[](int pos)
    {
        return subjects[pos];
    }
};

int main()
{
    marks harshit(80, 90, 88);
    cout << harshit[2];
}

class marks
{
    int mark;

public:
    marks(int m)
    {
        mark = m;
    }

    void tell_mark()
    {
        cout << mark << " marks\n";
    }

    marks operator()(int x)
    {
        mark = x;
        return *this;
    }
};

int main(){
    marks harshit(79);
    harshit.tell_mark();

    harshit(88);
    harshit.tell_mark();
}
