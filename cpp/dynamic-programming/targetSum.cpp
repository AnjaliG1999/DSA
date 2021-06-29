#include <bits/stdc++.h>

using namespace std;

int countSubsetSum (int *arr, int sum, int n) {
    int t[n+1][sum+1];
    
    t[0][0] = 1;
    
    for(int i=1; i<=n; i++) {
        t[0][i] = 0;
    }
    
    for(int i=1; i<=sum; i++) {
        t[i][0] = 1;
    }

    for(int i=1; i<=n; i++){
        for(int j=1; j<=sum; j++){
            if(arr[i-1] <= j){
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]];
            } else if(arr[i-1] > j){
                t[i][j] = t[i-1][j];
            }
        }
    }
    
    return t[n][sum];
}

int targetSum (int *arr, int n, int diff) {
    int sum = accumulate(arr, arr + n, 0);
    int s1 = (sum + diff) / 2;
    return countSubsetSum(arr, s1, n);
}

int main()
{
    int arr[] = {1, 1, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    int diff = 1;
    int result = targetSum(arr, n, diff);
    cout << result;
}
