#include <bits/stdc++.h>
using namespace std;

int isPalindromeRecursive (int start, string str, int end) {
    if(start==end) return 1;

    if(str[start] == str[end])
        return isPalindromeRecursive(start+1, str, end-1);
    return 0;
}

int isPalindrome (string str, int n) {
    if(n == 1) return 1;
    int flag = 0;
    for(int i=0; i<n/2; i++){
        if(str[i] != str[n-i-1]){
            flag = 0;
            break;
        } else
            flag = 1;
    }
    return flag;
}

int isPalindrome2 (string str, int n) {
    if(n == 1) return 1;
    int left = 0, right = n-1, flag = 0;
    while(left < right){
        if(str[left] != str[right]){
            flag = 0;
            break;
        } else{
            flag = 1;
            left++;
            right--;
        }
    }
    return flag;
}

int main(){
    string str = "abcba";
    int n = str.length();
//    int pal = isPalindromeRecursive(0, str, n-1);
//    int pal = isPalindrome(str, n);
    int pal = isPalindrome2(str, n);

    if(pal)
        cout << str << " is a palindrome";
    else
        cout << str << " is not a palindrome";
}