
#include <bits/stdc++.h>
using namespace std;

int findMinIterative(int arr[], int n){
    int minimum = arr[0];
    for(int i=1; i<n; i++) {
        if(minimum > arr[i])
            minimum = arr[i];
    }
    return minimum;
}

int findMaxIterative(int arr[], int n){
    int maximum = arr[0];
    for(int i=1; i<n; i++) {
        if(maximum < arr[i])
            maximum = arr[i];
    }
    return maximum;
}

int findMinRecursive(int arr[], int n){
    return (n==1) ? arr[0] : min(findMinRecursive(arr+1, n-1), arr[0]);
}

int findMaxRecursive(int arr[], int n){
    return (n==1) ? arr[0] : max(findMaxRecursive(arr+1, n-1), arr[0]);
}

int findMinLibrary(int arr[], int n){
    return *min_element(arr, arr+n);
}

int findMaxLibrary(int arr[], int n){
    return *max_element(arr, arr+n);
}

int main(){
    int arr[] = {1, 4, 6, 4, 6, 2, 7};
    int n = sizeof(arr)/ sizeof(arr[0]);
//    cout << n;

//    int minVal = findMinIterative(arr, n);
//    int maxVal = findMaxIterative(arr, n);

//    int minVal = findMinRecursive(arr, n);
//    int maxVal = findMaxRecursive(arr, n);

    int minVal = findMinLibrary(arr, n);
    int maxVal = findMaxLibrary(arr, n);

    cout << "Minimum: " << minVal << ", Maximum: " << maxVal;
}
