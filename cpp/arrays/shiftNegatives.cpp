#include <bits/stdc++.h>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0; i<n; i++)
        cout << arr[i] << " ";
}

int swap(int *a, int *b){
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
}

int shiftNegatives(int arr[], int n){
    int left = 0, right = n-1;
    while (left <= right) {
        if(arr[left] < 0 && arr[right] < 0)
            left++;
        else if(arr[left] > 0 && arr[right] < 0){
            swap(arr+left, arr+right);
            left++;
            right--;
        } else if(arr[left] > 0 && arr[right] > 0)
            right--;
        else{
            left++;
            right--;
        }
    }
    printArray(arr, n);
}

int quicksortPartition(int arr[], int n){
    int left = 0;
    for(int i=0; i<n; i++){
        if(arr[i] < 0){
            swap(arr[left], arr[i]);
            left++;
        }
    }
    printArray(arr, n);
}

int main(){
    int arr[] = {-12, 11, -13, -5, 6, -7, 5, -3, -6};
    int n = sizeof(arr)/ sizeof(arr[0]);
    cout << "Array: ";
    printArray(arr, n);
    cout << "\nAfter shifting negatives to the left: ";
//    shiftNegatives(arr, n);
    quicksortPartition(arr, n);
}