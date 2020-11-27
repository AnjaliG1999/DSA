#include <bits/stdc++.h>
using namespace std;

void binarySearch(int arr[], int n, int val) {
    cout << arr[i] << '\n';
    int low=0, high=n-1, flag = -1;

    while(low <= high){
        int mid=(low+high)/2;
        if(arr[mid] == val){
            flag = mid;
            break;
        } else if(arr[mid]>val)
            high = mid-1;
        else
            low = mid+1;
    }
    if(flag != -1)
        cout << "Value " << val << " found at position " << flag;
    else
        cout << "Value " << val << " not in array";
}

void binarySearch2(int arr[], int n, int val) {
    int low=0;
    for(int high=n/2; high>=1; high/=2){
        while(high+low < n && arr[high+low] <= val) low += high;
    }
    if(arr[low] == val)
        cout << "\nValue " << val << " found at position " << low;
    else
        cout << "\nValue " << val << " not in array";
}

int main(){
    int arr[10]; // {0, 1, 2, 3, 4, 7, 9, 10}
    int n, val; // 8,7
    cout << "Enter n and val: ";
    cin >> n >> val;
    cout << "Enter array: ";
    for(int i=0; i<n; i++)
        cin >> arr[i];

    binarySearch(arr, n, val);
    binarySearch2(arr, n, val);
    return 0;
}

