#include <bits/stdc++.h>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0; i<n; i++)
        cout << arr[i] << " ";
}

int findCommon (int arr1[], int arr2[], int arr3[], int l, int m, int n) {
    int i = 0, j = 0, k = 0;
    vector<int>common;

    while(i<l && j<m && k<n){
        if(arr1[i] == arr2[j] && arr1[i] == arr3[k]){
            common.push_back(arr1[i]);
            i++;
            j++;
            k++;
        } else if(arr1[i]<arr2[j] || arr1[i]<arr3[k])
            i++;
        else if(arr2[j]<arr3[k])
            j++;
        else
            k++;
    }
    cout << "\nCommon Elements: ";
    for (auto i: common)
        std::cout << i << ' ';
}

int main(){
    int arr1[] = {1, 5, 10, 20, 40, 80};
    int arr2[] = {6, 7, 20, 80, 100};
    int arr3[] = {3, 4, 15, 20, 30, 70, 80, 120};
    int l = sizeof(arr1)/ sizeof(arr1[0]);
    int m = sizeof(arr2)/ sizeof(arr2[0]);
    int n = sizeof(arr3)/ sizeof(arr3[0]);

    cout << "Array1: ";
    printArray(arr1, l);
    cout << "\nArray2: ";
    printArray(arr2, m);
    cout << "\nArray3: ";
    printArray(arr3, n);

    findCommon(arr1, arr2, arr3, l, m, n);
}