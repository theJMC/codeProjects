#include <iostream>
#include <time.h>
#include <fstream>
#include <string>
#include <conio.h> 
#include <ctime>
#include <picosha2.h>
using namespace std;

string src_str = "The quick brown fox jumps over the lazy dog";
string hash_hex_str;
picosha2::hash256_hex_string(src_str, hash_hex_str);
cout << hash_hex_str << endl;
//this output is "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"