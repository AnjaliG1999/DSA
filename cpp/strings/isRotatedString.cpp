#include <bits/stdc++.h>
using namespace std;

int isRotated (string str1, string str2) {
    string temp = str1+str1;
    if (temp.find(str2) != string::npos)
        return true;
    return false;
}

int main(){
    string str1 = "ABCD", str2 = "CDAB";
    int rotated = isRotated(str1, str2);
    if(rotated)
        cout << str2 << " is a rotated string of " << str1;
    else
        cout << str2 << " is not a rotated string of " << str1;
}