#include <bits/stdc++.h>
using namespace std;

string reversePointer (string str, int n) {
    for(int i=0; i<n/2; i++){
        swap(str[i], str[n - i - 1]);
    }
    return str;
}

string reverseFunction (string str, int n) {
    reverse(str.begin(), str.end());
    return str;
}

string reverseFunction2 (string str, int n) {
    string rev = string(str.rbegin(), str.rend());
    return rev;
}

string reverseLoop (string str, int n) {
    string rev = str;
    for(int i=0; i<n; i++){
        rev[n-i-1] = str[i];
    }
    return rev;
}

int main(){
    string str = "hello";
    int n = str.length();

    cout << "String: " << str << "\nReversed String: ";
//    string rev = reverseFunction(str, n);
//    string rev = reversePointer(str, n);
//    string rev = reverseFunction2(str, n);
    string rev = reverseLoop(str, n);
    cout << rev;
}