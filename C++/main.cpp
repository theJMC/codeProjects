#include <iostream>
#include <time.h>
#include <fstream>
#include <string>
#include <conio.h> 
#include <ctime>
// #include <picosha2.h>

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

// string sha256() {
//     string src_str = "The quick brown fox jumps over the lazy dog";
//     string hash_hex_str;
//     picosha2::hash256_hex_string(src_str, hash_hex_str);
//     cout << hash_hex_str << endl;
//     //this output is "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"
// }

int login() {
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
        return 200;
    }
    else if (userAttempt == username) {
        if (passAttempt != password) {
            cout << "Password Incorrect";
            return 401;
        }
    }
    else {
        cout << "User not in my Database...";
        return 404;
    }
    sleepcp(1000);


    return 0;
    
}

int reg();
    cout << "Registering" << endl << "Username: ";
    cin >> username;
    cout << endl << "Password" << endl;
    cin >> password;
    system('cls');
    cout << "Done!";
    sleepcp(1000);

int start() {
    // start the actual program
    system("cls");
    //TEMPORARY
    
    // title
    cout << "Welcome to the JAM Login Script (C++ Edition)" << endl;
    sleepcp(1000);
    system("cls");
    // sets weather the user wants to exit
    bool exit;
    // response code
    int code;
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
            return login();
        }
        else if(response == "2") {
            cout << "Registering..." << endl;
            sleepcp(1000);
            return 501;
        }
        else if(response == "3") {
            exit = true;
            return 103;
        }
        // error function
        else {
            cout << "I can't read this alien text you speak!" << endl;
            sleepcp(1000);
            return 400;
        }
        system("cls");
    }
}



int main() {

    // init function
    cout << '\n';
    start();
}
/* Error Codes:
1xx Informational
103 - User Terminated

2xx Sucessful
200 - OK
201 - Created

4xx Client Error
400 - Bad Request
401 - Unauthorised
404 - Not Found

5xx Server Error
501 - Not Implemented
*/ 
