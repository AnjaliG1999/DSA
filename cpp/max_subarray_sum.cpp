#include <bits/stdc++.h>
using namespace std;

void Sum1(int arr[], int n){
    int best = 0;

    for(int start=0; start<n; start++){
        for(int stop=start; stop<n; stop++){
            int sum = 0;
            for(int index=start; index<=stop; index++)
                sum += arr[index];
            best = max(best, sum);
        }
    }
    cout << "Algo1: " << best << "\n\tTime Complexity- O(n^3), Space Complexity- O(1)\n\n";
}

void Sum2(int arr[], int n){
    int best = 0;

    for(int start=0; start<n; start++){
        int sum = 0;
        for(int index=start; index<n; index++){
            sum += arr[index];
            best = max(best, sum);
        }
    }
    cout << "Algo2: " << best << "\n\tTime Complexity- O(n^2), Space Complexity- O(1)\n\n";
}

void Sum3(int arr[], int n){
    int best = 0, sum = 0;
    for(int index=0; index<n; index++){
        sum = max(arr[index], sum+arr[index]);
        best = max(sum, best);
    }
    cout << "Algo3: " << best << "\n\tTime Complexity- O(n), Space Complexity- O(1)\n\n";
}

int main() {
    int arr[10]; // {-1, 2, 4, -3, 5, 2, -5, 2}
    int n; // 8
    cout << "Enter n: ";
    cin >> n;
    cout << "\nEnter array: \n";
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    cout << "\nMaximum subarray sum:\n\n";

    Sum1(arr, n);
    Sum2(arr, n);
    Sum3(arr, n);
}
