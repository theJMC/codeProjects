#include <iostream>
#include <time.h>
#include <fstream>
#include <string>
#include <conio.h>

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

string login() {
    // TEMPORARY
    string username;
    username = "root";
    string password;
    password = "toor";
    // TEMPORARY
    string userAttempt;
    string passAttempt;
    char ch;
    // start the login sequence
    system("cls");
    cout << "Logging In";
    sleepcp(1000);
    cout << ".";
    sleepcp(1000);
    cout << ".";
    sleepcp(1000);
    cout << ".";
    sleepcp(1000);
    system("cls");
    cout << "Username: ";
    cin >> userAttempt;
    cout << "Password: ";
    ch = _getch();
    while(ch != 13) {//character 13 is enter
        passAttempt.push_back(ch);
        cout << '*';
        ch = _getch();
    }
    cout << endl;
    if (userAttempt == username && passAttempt == password) {
        cout << "You Successfully Logged in!";
    }
    else if (userAttempt == username) {
        if (passAttempt != password) {
            cout << "Password Incorrect";
        }
    }
    else {
        cout << "User not in my Database...";
    }
    sleepcp(1000);


    return username;
}

int start() {
    // start the actual program
    system("cls");
    // title
    cout << "Welcome to the JAM Login Script (C++ Edition)" << endl;
    sleepcp(1000);
    system("cls");
    // sets weather the user wants to exit
    bool exit;
    // allows for continuos cycling
    while(!exit) {
        string response;
        system("cls");
        cout << "1. Login" << endl;
        cout << "2. Register" << endl;
        cout << "3. Exit" << endl;
        cout << endl << "Option: ";
        cin >> response;
        if(response == "1") {
            login();
        }
        else if(response == "2") {
            cout << "Registering..." << endl;
            sleepcp(1000);
        }
        else if(response == "3") {
            exit = true;
        }
        // error function
        else {
            cout << "I can't read this alien text you speak!" << endl;
            sleepcp(1000);
        }
        system("cls");
    }
    return 0;
}



int main() {
    // init function
    start();
}