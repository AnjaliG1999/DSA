#include <bits/stdc++.h>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0; i<n; i++)
        cout << arr[i] << " ";
}

void printVector(vector<int> v) {
    for(auto elem : v){
        cout << elem << " ";
    }
}

void nearestGreaterElementRight (int arr[], int n) {
    vector<int> output;
    stack<int> s;

    for(int i=n-1; i>=0; i--) {
        while(s.size() > 0 && s.top() <= arr[i])
            s.pop();
        if (s.size() == 0)
            output.push_back(-1);
        else
            output.push_back(s.top());

        s.push(arr[i]);
    }
    reverse(output.begin(), output.end());
    printVector(output);
}

void nearestGreaterElementLeft (int arr[], int n) {
    vector<int> output;
    stack<int> s;

    for(int i=0; i<n; i++) {
        while(s.size() > 0 && s.top() <= arr[i])
            s.pop();
        if (s.size() == 0)
            output.push_back(-1);
        else
            output.push_back(s.top());

        s.push(arr[i]);
    }
    printVector(output);
}

int main(){
    int arr[] = {10, 5, 11, 6, 20, 12};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "The next greatest elements of ";
    printArray(arr, n);
    cout << "to right are ";
    nearestGreaterElementRight(arr, n);

    cout << "\nThe next greatest elements of ";
    printArray(arr, n);
    cout << "to left are ";
    nearestGreaterElementLeft(arr, n);
}