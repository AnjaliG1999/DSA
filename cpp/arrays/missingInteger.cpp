#include <bits/stdc++.h>
using namespace std;

int missingInteger(vector<int>& arr, int n){
    int naturalSum = n * (n+1) / 2;
    int missing = naturalSum - accumulate(arr.begin(), arr.end(), 0);
    return missing;
}

int missingIntegerModified(vector<int>& arr, int n){
    int total = 1;
    for(int i=2; i<n; i++){
        total += i;
        total -= arr[i-2];
    }
    return total;
}

int missingIntegerBit(vector<int>& arr, int n){
    int x1 = arr[0], x2 = 1;
    for(int i=1; i<n; i++)
        x1 ^= arr[i];
    for(int i=2; i<n+1; i++)
        x2 ^= i;
    return x1 ^ x2;
}

int main(){
    int n = 8;
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(6);
    v.push_back(7);
    v.push_back(8);

//    int missing = missingInteger(v, n);
//    int missing = missingIntegerModified(v, n);
    int missing = missingIntegerBit(v, n);
    cout << "Missing number: " << missing;
}