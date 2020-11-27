#include <bits/stdc++.h>
using namespace std;

void printVector(vector<int> v) {
    for(int i=0; i<v.size(); i++)
        cout << v.at(i) << ' ';
}

void sortVector(){
    cout << "Vector:\n";
    vector<int> v = {4,2,5,3,5,8,3};
    cout << "Before sorting: ";
    printVector(v);

    sort(v.begin(), v.end());
    cout << "\nAfter sorting in ascending order: ";
    printVector(v);

    sort(v.rbegin(), v.rend());
    cout << "\nAfter sorting in descending order: ";
    printVector(v);
}

void sortArray(){
    int arr[] = {4,2,5,3,5,8,3};
    int n = 7;

    cout << "\n\nArray:\n";
    cout << "Before sorting: ";
    for(int i=0; i<n; i++)
        cout << arr[i] << ' ';

    sort(arr, arr+n);
    cout << "\nAfter sorting in ascending order: ";
    for(int i=0; i<n; i++)
        cout << arr[i] << ' ';

    sort(arr, arr+n, greater<int>());
    cout << "\nAfter sorting in descending order: ";
    for(int i=0; i<n; i++)
        cout << arr[i] << ' ';
}

void sortString(){
    string str = "This_is_an_unsorted_string";

    cout << "\n\nString:\n";
    cout << "Before sorting: " << str;

    sort(str.begin(), str.end());
    cout << "\nAfter sorting in ascending order: " << str;

    sort(str.rbegin(), str.rend());
    cout << "\nAfter sorting in descending order: " << str << "\n";
}

int main(){
    sortVector();
    sortArray();
    sortString();

    return 0;
}
