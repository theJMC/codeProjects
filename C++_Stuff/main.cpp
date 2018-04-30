#include <iostream>
#include <time.h>

using namespace std;

void sleepcp(int milliseconds);

void sleepcp(int milliseconds) // Cross-platform sleep function
{
    clock_t time_end;
    time_end = clock() + milliseconds * CLOCKS_PER_SEC/1000;
    while (clock() < time_end)
    {
    }
}

int start() {
    system("cls");
    cout << "Welcome to the JAM Login Script (C++ Edition)" << endl;
    sleepcp(1000);
    system("cls");
    bool exit;
    while(!exit) {
        string response;
        system("cls");
        cout << "1. Login" << endl;
        cout << "2. Register" << endl;
        cout << "3. Exit" << endl;
        cout << endl << "Option: ";
        cin >> response;
        if(response == "1") {
            cout << "Logging In..." << endl;
            sleepcp(1000);
        }
        else if(response == "2") {
            cout << "Registering..." << endl;
            sleepcp(1000);
        }
        else if(response == "3") {
            exit = true;
        }
        else {
            cout << "I can't read this alien text you speak!" << endl;
            sleepcp(1000);
        }
        system("cls");
    }
    return 0;
}

int main() {
    start();
}