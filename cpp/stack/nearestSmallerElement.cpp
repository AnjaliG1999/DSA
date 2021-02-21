#include <bits/stdc++.h>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0; i<n; i++)
        cout << arr[i] << " ";
}

int nearestSmallerElementRight (int arr[], int n) {
    int output[n];
    stack<int> s;

    for(int i=n-1; i>=0; i--) {
        while(s.empty() == false && arr[i] < s.top())
            s.pop();
        if (s.empty())
            output[i] = -1;
        else
            output[i] = s.top();

        s.push(arr[i]);
    }
    printArray(output, n);
}

int nearestSmallerElementLeft (int arr[], int n) {
    int output[n];
    stack<int> s;

    for(int i=0; i<n; i++) {
        while(s.empty() == false && arr[i] < s.top())
            s.pop();
        if (s.empty())
            output[i] = -1;
        else
            output[i] = s.top();

        s.push(arr[i]);
    }
    printArray(output, n);
}

int main(){
    int arr[] = {10, 5, 11, 6, 20, 12};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "The next greatest elements of ";
    printArray(arr, n);
    cout << "to right are ";
    nearestSmallerElementRight(arr, n);

    cout << "\nThe next greatest elements of ";
    printArray(arr, n);
    cout << "to left are ";
    nearestSmallerElementLeft(arr, n);
}