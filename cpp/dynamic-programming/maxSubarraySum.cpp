#include <bits/stdc++.h>
using namespace std;

int maxSubarrayCubic (int arr[], int n) {
    int maxSum = -9999;

    for(int left=0; left<n; left++) {
        for(int right=left; right<n; right++) {
            int window_sum = 0;

            for(int el=left; el<=right; el++)
                window_sum += arr[el];

            if(window_sum > maxSum)
                maxSum = window_sum;
        }
    }

    return maxSum;
}

int maxSubarrayQuadratic (int arr[], int n) {
    int maxSum = -9999;

    for(int left=0; left<n; left++) {
        int running_sum = 0;
        for(int right=left; right<n; right++) {
            running_sum += arr[right];

            maxSum = max(maxSum, running_sum);
        }
    }

    return maxSum;
}

int maxSubarrayLinear (int arr[], int n) {
    int maxSum = arr[0], running_sum = arr[0];

    for(int idx=1; idx<n; idx++) {
        running_sum = max(running_sum + arr[idx], arr[idx]);
        maxSum = max(maxSum, running_sum);
    }

    return maxSum;
}

int main(){
    int arr[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
//    int maxSum = maxSubarrayCubic(arr, n);
//    int maxSum = maxSubarrayQuadratic(arr, n);
    int maxSum = maxSubarrayLinear(arr, n);
    cout << maxSum;
}