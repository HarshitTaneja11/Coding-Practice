#include <iostream>
#include <string>

using namespace std;

// class arrays
// {

//     int arr[10];

// public:
//     void setarray()
//     {
//         for (int i = 0; i < 10; i++)
//         {
//             cin >> arr[i];
//         }
//     }

//     void display(){
//         for (int i = 0; i < 10; i++)
//         {
//             cout << arr[i] << " ";
//         }

//     }

//     void sort()
//     {
//         int n = 10;
//         for (int i = 0; i < n - 1; i++)
//         {
//             for (int j = 0; j < n - i - 1; j++)
//             {
//                 if (arr[j] > arr[j + 1])
//                 {
//                     int temp = arr[j];
//                     arr[j] = arr[j + 1];
//                     arr[j + 1] = temp;
//                 }
//             }
//         }

//     }
// };

// int main()
// {
//     arrays a;
//     a.setarray();
//     a.sort();
//     cout << "The sorted array is: ";
//     a.display();
// }

// class emp
// {
//     string name;
//     int age;

// public:
//     void getdata();
//     void showdata();
// };

// void emp ::getdata()
// {
//     cout << "Enter name: ";
//     cin.ignore();
//     getline(cin, name);
//     cout << "Enter Age: ";
//     cin >> age;

// }

// void emp ::showdata()
// {
//     cout << name << endl;
//     cout << age << endl;
// }

// int main()
// {
//     emp array[3];
//     for (int i = 0; i < 3; i++)
//     {
//         cout << "enter detail for employee number: " << i + 1 << endl;
//         array[i].getdata();
//     }

//     for (int i = 0; i < 3; i++)
//     {
//         array[i].showdata();
//     }
// }

// class convert
// {
// public:
//     int num;

//     void increment(convert &obj) //to show pass by value and pass by reference
//     {
//         obj.num = obj.num * 2;
//         cout << "The value of the object in function is = " << obj.num << endl;
//     }
// };

// int main()
// {
//     convert obj1;
//     obj1.num = 3;
//     obj1.increment(obj1);
//     cout << "The value of object in main is = " << obj1.num << endl;
// }

// class myclass
// {
//     static int a;
//     int b;

// public:
//     static int c;
//     void set(int i, int j)
//     {
//         a++;
//         b = i;
//         c = j;
//     }
//     void get()
//     {
//         cout << "Static a: " << a << endl;
//         cout << "Non - Static b: " << b << endl;
//         cout << "Static c: " << c << endl;
//     }
// };

// int myclass ::a = 33;
// int myclass ::c;

// int main()
// {
//     cout << "By default static C = " << myclass ::c << endl;
//     myclass o1, o2;
//     o1.set(44, 55);
//     o1.get();

//     o2.set(11, 22);
//     o2.get();
//     return 0;
// }

// C++ Program to show the working of
// static member functions

// #include <iostream>
// using namespace std;

// class Box
// {
//     private:
//     static int length;
//     static int breadth;
//     static int height;

//     public:

//     static void print()
//     {
//         cout << "The value of the length is: " << length << endl;
//         cout << "The value of the breadth is: " << breadth << endl;
//         cout << "The value of the height is: " << height << endl;
//     }
// };

// // initialize the static data members

// int Box :: length = 10;
// int Box :: breadth = 20;
// int Box :: height = 30;

// // Driver Code

// int main()
// {

//     Box b;

//     cout << "Static member function is called through Object name: \n" << endl;
//     b.print();

//     cout << "\nStatic member function is called through Class name: \n" << endl;
//     Box::print();

//     return 0;
// }

// class shared
// {
//     static int resource;   // shared among ALL objects of this class

// public:
//     static int getResource()
//     {
//         if (resource)         // if resource is already in use
//             return 0;         // deny access
//         else
//         {
//             resource = 1;     // mark resource as taken
//             return 1;         // grant access
//         }
//     }

//     void freeResource()
//     {
//         resource = 0;         // release resource (make available again)
//     }
// };

// int shared::resource;   // definition of static variable (defaults to 0)

// int main()
// {
//     shared o1, o2;

//     if (o1.getResource())
//         cout << "\no1 has resource.";

//     if (!shared::getResource())
//         cout << "\no2 access denied.";

//     o1.freeResource();

//     if (shared::getResource())
//         cout << "\no2 has resource.";

//     return 0;
// }

// int main()
// {  int a = 10;
//    int &ref = a;
//    cout << a << " " << ref << endl;
//    ref += 5;
//    cout << a << " " << ref << endl;
//    return 0;
// }

// #include <iostream>
// using namespace std;
// class ABC
// {
// private:
//     char charray[10];

// public:
//     void reveal()
//     {
//         cout << "\nMy object's address is " << this;
//     }
// };
// int main()
// {
//     ABC w1, w2;
//     w1.reveal();
//     w2.reveal();
//     cout << endl;
//     return 0;
// }

// class example
// {
// private:
//     int a, b;

// public:
//     example();          // Default Constructor
//     example(int, int);  // Parameterized Constructor
//     example(example &); // Copy Constructor
//     void display();
// };

// example::example()
// {
//     cout << "Constructor is called" << endl;
// }

// example::example(int x, int y)
// {
//     a = x;
//     b = y;
// }

// example::example(example &object)
// {
//     a = object.a;
//     b = object.b;
// }
// void example::display()
// {
//     cout << a << endl
//          << b;
// }
// int main()
// {
//     example e1;
//     example e2(4, 5);
//     example e3(e2);
//     e3.display();
//     return 0;
// }

// class student
// {
// public:
//     string name;

//     student()
//     {
//         cout << "Default Constructor";
//     }
//     student(string name)
//     {
//         this->name = name;
//         cout << "Paramter Constructor";
//     }
// };

// int main(){
//     student s1(" Harshit Taneja");
// }

// class print
// {
// public:
//     void show(int x)
//     {
//         cout << "Integer = " << x << endl;
//     }

//     void show(char ch){
//         cout << "Char = " << ch << endl;
//     }
// };

// int main(){
//     print p1;
//     p1.show('H ');
// }

// class person
// {
// public:
//     string name;
//     int age;

//     person(string name, int age)
//     {
//         this->name = name;
//         this->age = age;
//     }

//     ~person()
//     {
//         cout << "Parent Desructor" << endl;
//     }
// };

// class student : public person
// {
// public:
//     int roll_no;

//     student(string name, int age, int roll_no) : person(name, age)
//     {
//         this->roll_no = roll_no;
//         cout << "Child constructor" << endl;
//     }

//     ~student()
//     {
//         cout << "Child Desructor" << endl;
//     }

//     void getinfo()
//     {
//         cout << name << endl;
//         cout << age << endl;
//         cout << roll_no << endl;
//     }
// };

// class teacher
// {
// public:
//     string subject;
//     int salary;
// };

// class TA : public student, public teacher{

// };

// class graduated : public student
// {
// public:
//     string company;
// }

// int
// main()
// {
//     student st1("Harshit Taneja", 19, 123);
//     st1.getinfo();

//     TA t1;
    
// }


