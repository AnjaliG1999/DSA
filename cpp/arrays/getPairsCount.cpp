#include <bits/stdc++.h>
using namespace std;

int getPairsCount(int arr[], int n, int val){
    int count = 0;
    int viewed[150] = {0};
    
    for(int i=0; i<n; i++){
        viewed[arr[i]]++;
    }
    
    for(int i=0; i<n; i++){
        count += viewed[val - arr[i]];
        if(val - arr[i] == arr[i])
            count--;
    }
    return count/2;
}

int getPairsCountBrute(int arr[], int n, int val){
    int count = 0;
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            if(arr[i] + arr[j] == val)
                count++;
        }
    }
    return count;
}

int main(){
    int arr[] = {1, 5, 7, -1, 5};
    int n = sizeof(arr)/ sizeof(arr[0]);
    int val = 6;
    
    int pairs = getPairsCount(arr, n, val);
    // int pairs = getPairsCountBrute(arr, n, val);
    cout << "There are " << pairs << " pairs in the array with the sum " << val;
}