#include <bits/stdc++.h>
using namespace std;

int main(){
    string str1 = "Hello";
    string str2 = str1+str1;

    cout << "String1: " << str1 << "\n" << "String2 (String1+String1): " << str2 << "\n";

    str2[5] = 'h';
//    str2[5] = "h"; error: invalid conversion
    cout << "String 2: " << str2 << "\n";

    string str3 = str2.substr(5, 4);
    cout << "String 3: " << str3 << "\n";

    cout << "String 3 is at position " << str2.find(str3) << " in String 2\n";
}
