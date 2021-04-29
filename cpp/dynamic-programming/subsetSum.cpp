#include <bits/stdc++.h>

using namespace std;

bool subsetSum (int *arr, int n, int sum){
    if(n == 0) return false;
    if(sum == 0) return true;
    
    if(arr[n-1] <= sum){
        return subsetSum(arr, n-1, sum) || subsetSum(arr, n-1, sum-arr[n-1]);
    }
    return subsetSum(arr, n-1, sum);
}

int t[11][51];

bool subsetSumMemoized (int *arr, int n, int sum){
    if(n == 0) return false;
    if(sum == 0) return true;
    
    if(t[n][sum] != -1) return t[n][sum];
    
    if(arr[n-1] <= sum){
        return t[n][sum] = subsetSum(arr, n-1, sum) || subsetSum(arr, n-1, sum-arr[n-1]);
    }
    return t[n][sum] = subsetSum(arr, n-1, sum);
}

bool subsetSumTopDown (int *arr, int n, int sum){
    for(int i=0; i<=n; i++){
        for(int j=0; j<=sum; j++){
            if(i == 0) t[i][j] = false;
            if(j == 0) t[i][j] = true;
            
            else if (arr[i-1] <= j) t[i][j] = t[i-1][j] || t[i-1][j-arr[i-1]];
            else t[i][j] = t[i-1][j];
        }
    }
    return t[n][sum];
}

int main()
{
    int arr[] = {3, 34, 4, 12, 5, 2};
    int sum = 30;
    int n = sizeof(arr)/ sizeof(arr[0]);
    memset(t, -1, sizeof(t));
    
    // bool result = subsetSum(arr, n, sum);
    // bool result = subsetSumMemoized(arr, n, sum);
    bool result = subsetSumTopDown(arr, n, sum);
    if(result)
        cout << "Found a subset with given sum";
    else
        cout << "No subset with given sum";      
}