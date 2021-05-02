// Online C++ compiler to run C++ program online
#include <bits/stdc++.h>

using namespace std;

int t[11][21];

bool subsetSum (int *arr, int sum, int n) {
    for(int i=0; i<=n; i++){
        for(int j=0; j<=sum; j++){
            if(j == 0) t[i][j] = false;
            if(i == 0) t[i][j] = true;
            
            else if(arr[i-1] <= j){
                t[i][j] = t[i-1][j] || t[i-1][j-arr[i-1]];
            } else {
                t[i][j] = t[i-1][j];
            }
        }
    }
    return t[n][sum];
}

bool equalSum (int *arr, int n) {
    int total = 0;
    total = accumulate(arr, arr+n, total);
    if(total % 2 != 0) return false;
    return subsetSum(arr, total/2, n);
}

int main() {
    int arr[] = {1, 5, 5, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    memset(t, -1, sizeof(t));
    
    bool result = equalSum(arr, n);
    if(result)
        cout << "Can be divided into two subsets of equal sum";
    else
        cout << "Can not be divided into two subsets of equal sum";
}