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

int frequency1(int arr[], int n){
    // int sortedArr[n];
    int count0 = 0, count1 = 0, count2 = 0;
    for(int i=0; i<n; i++){
        if(arr[i]==0)
            count0++;
        else if(arr[i]==1)
            count1++;
        else
            count2++;
    }

    for(int i=0; i<count0; i++)
        arr[i] = 0;
    for(int i=count0; i<count0+count1; i++)
        arr[i] =1;
    for(int i=count0+count1; i<n; i++)
        arr[i] = 2;

    printArray(arr, n);
}

int dutchNationalFlagAlgo(int arr[], int n) {
    int low = 0, mid = 0, high = n-1;
    while(mid <= high) {
        if(arr[mid]==0){
            swap(arr+mid, arr+low);
            low++;
            mid++;
        } else if(arr[mid]==1){
            mid++;
        } else {
            swap(arr+mid, arr+high);
            high--;
        }
    }

    printArray(arr, n);
}

int main(){
    int arr[] = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1};
    int n = sizeof(arr)/ sizeof(arr[0]);
    cout << "Array: ";
    printArray(arr, n);
    cout << "\nSorted array: ";
    // frequency1(arr, n);
    dutchNationalFlagAlgo(arr, n);
}