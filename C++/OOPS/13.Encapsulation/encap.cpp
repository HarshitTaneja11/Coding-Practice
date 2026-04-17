#include <iostream>
#include <string>
#include <vector>

using namespace std;

class BankAccount
{
private:
    string accountnumber;
    double balance;

public:
    BankAccount(string accnum, double initialbalance)
    {
        accountnumber = accnum;
        balance = initialbalance;
    }

    double getbalance()
    {
        return balance;
    }

    // Method to deposit Money
    void deposit(double amount)
    {
        if (amount > 0)
        {
            balance = balance + amount;
            cout << "Updated balance is = " << balance << endl;
        }
        else
        {
            cout << "Invalid deposit amount";
        }
    }

    void withdraw(double money)
    {
        if (money > balance)
        {
            cout << "Insufficient Balance";
        }
        else if (money <= balance && money > 0)
        {
            balance = balance - money;
        }
    }
};

int main()
{
    BankAccount myAccount("1024030826", 100000);

    myAccount.getbalance();

    myAccount.deposit(50000);
    myAccount.withdraw(1000);
    myAccount.deposit(500);
}