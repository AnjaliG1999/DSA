#include <bits/stdc++.h>
using namespace std;

unordered_map<int, int> dict;

void findFrequency(int arr[], int n){
    for(int i=0; i<n; i++)
        dict[arr[i]]++;
}

int frequency1(int arr[], int val, int n){
    findFrequency(arr, n);
    return dict[val];
}

int frequency2(int arr[], int val, int n){
    int count = 0;
    for(int i=0; i<n; i++)
        arr[i]==val ? count++ : NULL;
    return count;
}

int main(){
    int arr[] = {1, 3, 5, 3, 6, 7, 1, 0, 3};
    int n = sizeof(arr)/ sizeof(arr[0]);
    int val, freq;
    cout << "Enter value to count: ";
    cin >> val;

//    freq = frequency1(arr, val, n);
    freq = frequency2(arr, val, n);
    cout << "No. of " << val << "'s in array: " << freq;
}