// Online C++ compiler to run C++ program online
#include <bits/stdc++.h>

using namespace std;

int countSubsetSum (int *arr, int sum, int n) {
    int t[n+1][sum+1];

    for(int i=0; i<=n; i++){
        for(int j=0; j<=sum; j++){
            if(i == 0) t[i][j] = 0;
            if(j == 0) t[i][j] = 1;
            
            else if(arr[i-1] <= j){
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]];
            } else {
                t[i][j] = t[i-1][j];
            }
        }
    }
    return t[n][sum];
}

int main() {
    int arr[] = {1, 1, 1, 1};
    int sum = 1;
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // memset(t, 0, sizeof(t));
    
    int result = countSubsetSum(arr, sum, n);
    cout << result;
}