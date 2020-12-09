#include <bits/stdc++.h>
using namespace std;

int frequency1(int arr[], int n){
    int sortedArr[n];
    int count0 = 0, count1 = 0, count2 = 0;
    for(int i=0; i<n; i++){
        if(arr[i]==0)
            count0++;
        else if(arr[i]==1)
            count1++;
        else
            count2++;
    }

    for(int i=0; i<count0; i++)
        sortedArr[i] = 0;
    for(int i=count0; i<count0+count1; i++)
        sortedArr[i] =1;
    for(int i=count0+count1; i<n; i++)
        sortedArr[i] = 2;

    for(int i=0; i<n; i++)
        cout << sortedArr[i] << " ";
}

int main(){
    int arr[] = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1};
    int n = sizeof(arr)/ sizeof(arr[0]);
//    cout << frequency1(arr, n);
    frequency1(arr, n);
}