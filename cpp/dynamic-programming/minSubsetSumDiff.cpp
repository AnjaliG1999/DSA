#include <bits/stdc++.h>

using namespace std;

int t[11][51];

bool subsetSum (int *arr, int n, int sum){
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

int subsetSumDiff (int *arr, int n){
    vector<int> val;
    
    int total = accumulate(arr, arr + n, 0);
    int minm = total;
    for (int i=0; i<= total/2; i++){
        if(subsetSum(arr, n-1, i)){
            val.push_back(i);
        }
    }
    for(auto& it : val){
        if(total- 2* it < minm) {
            minm = total - 2 * it;
        }
    }
    return minm;
}

int main()
{
    int arr[] = {10, 20, 15, 5, 25};
    int n = sizeof(arr)/ sizeof(arr[0]);
    memset(t, -1, sizeof(t));

    int result = subsetSumDiff(arr, n);
    cout << result;
}