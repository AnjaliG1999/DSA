#include <bits/stdc++.h>
using namespace std;

void swap(int arr[], int start, int end){
    arr[start] = arr[start] ^ arr[end];
    arr[end] = arr[start] ^ arr[end];
    arr[start] = arr[start] ^ arr[end];
}
void printArray(int arr[], int n){
    for(int i=0; i<n; i++)
        cout << arr[i] << " ";
}

int reverseIterative(int arr[], int start, int end, int n){
    while(start < end) {
        swap(arr, start, end);
        start++;
        end--;
    }
}

int reverseRecursive(int arr[], int start, int end){
    if(start >= end)
        return NULL;
    swap(arr, start, end);
}

int main(){
    int arr[] = {1, 4, 6, 4, 6, 2, 7};
    int n = sizeof(arr)/ sizeof(arr[0]);

    cout << "Array: ";
    printArray(arr, n);
    cout << "\nReversed array: ";
//    reverseIterative(arr, 0, n-1, n);
    reverseRecursive(arr, 0, n-1);
    printArray(arr, n);
}
