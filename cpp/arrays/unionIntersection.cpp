#include <bits/stdc++.h>
using namespace std;

void printArray(int arr[], int n){
    for(int i=0; i<n; i++)
        cout << arr[i] << " ";
}

// int printMap(int map<int, bool> const &m) {
//     for (const auto& x : m) {
//         cout << x.first << "  ";
//     }
// }

int fillDictUnion (int arr1[], int arr2[], int m, int n){
    map<int, bool> unionDict;
    for(int i=0; i<m; i++){
        if (unionDict.find(arr1[i]) == unionDict.end()) 
            unionDict.insert(pair<int, bool>(arr1[i], true));
    }
    
    for(int i=0; i<n; i++){
        if (unionDict.find(arr2[i]) == unionDict.end()) 
            unionDict.insert(pair<int, bool>(arr2[i], true));
    }
    
    for (const auto& x : unionDict) {
        cout << x.first << " ";
    }
}

int fillDictIntersection (int arr1[], int arr2[], int m, int n){
    map<int, bool> intersectionDict;
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if (arr1[i] == arr2[j])
                intersectionDict.insert(pair<int, bool>(arr1[i], true));
        }
    }

    for (const auto& x : intersectionDict) {
        cout << x.first << " ";
    }
}

int arrUnion (int arr1[], int arr2[], int m, int n) {
    m > n ? fillDictUnion(arr1, arr2, m, n): fillDictUnion(arr2, arr1, n, m);
}

int arrIntersection (int arr1[], int arr2[], int m, int n) {
    m > n ? fillDictIntersection(arr1, arr2, m, n): fillDictIntersection(arr2, arr1, n, m);
}

int main(){
    int arr1[] = {1, 5, 3, 0, 2, 1, 9};
    int arr2[] = {4, 2, 5, 7};
    int m = sizeof(arr1)/ sizeof(arr1[0]);
    int n = sizeof(arr2)/ sizeof(arr2[0]);
    
    cout << "Array1: ";
    printArray(arr1, m);
    cout << "\nArray2: ";
    printArray(arr2, n);
    
    cout << "\nUnion: ";
    arrUnion(arr1, arr2, m, n);
    cout << "\nIntersection: ";
    arrIntersection(arr1, arr2, m, n);
}