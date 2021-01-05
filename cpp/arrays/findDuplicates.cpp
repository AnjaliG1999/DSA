#include <bits/stdc++.h>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0; i<n; i++)
        cout << arr[i] << " ";
}

void printDuplicates(set<int>s){
    if (s.size() > 1){
        cout << "\nDuplicates: ";
        for (auto i: s)
        cout << i << ' ';
    }
    else
        cout << "\nThere is no duplicate element in the array";

}

int findDuplicates (int arr[], int n) {
    map<int, bool> dict;
    set<int> duplicates;

    for(int i=0; i<n; i++){
        if (dict.find(arr[i]) != dict.end())
            duplicates.insert(arr[i]);
        else
            dict.insert(pair<int, bool>(arr[i], true));
    }
    printDuplicates(duplicates);
}

int findDuplicates2 (int arr[], int n) {
    set<int> duplicates;

    for(int i=0; i<n; i++){
        arr[arr[i]%n] += n;
    }

    for(int i=0; i<n; i++){
        if (arr[i] > 2*n)
            duplicates.insert(i);
    }
    printDuplicates(duplicates);
}

int main(){
    int arr[] = {1, 2, 3, 6, 3, 6, 1, 1};
    int n = sizeof(arr)/ sizeof(arr[0]);

    cout << "Array: ";
    printArray(arr, n);

//    findDuplicates(arr, n);
    findDuplicates2(arr, n);
}