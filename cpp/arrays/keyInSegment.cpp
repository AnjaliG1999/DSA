#include <bits/stdc++.h>
using namespace std;

int isPresent(int arr[], int k, int x, int n){
    int i = 0;
    while(i < n/k){
        int j = 0;
        while(j < k){
            if(arr[k*i+j] == x)
                break;
            j++;
        }
        if(j == k)
            return false;
        i++;
    }
    
    if (k*i == n)
        return true;

    for(int j = k*i+1; j < n; j++){   
        if(x == arr[j])
            return true;
    }
    return false;
}

int main() {
    int arr[] = {3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3, 4, 8};
    int k = 3, x = 3;
    int n = sizeof(arr)/sizeof(arr[0]);

    if(isPresent(arr, k, x, n))
        cout << x << " is present in every segment of size " << k;
    else
        cout << x << " is not present in every segment of size " << k;
}