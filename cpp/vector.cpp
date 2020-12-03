#include <bits/stdc++.h>
using namespace std;

void printVector(vector<int> v){
    for(auto val: v)
        cout << val << " ";
}

void printVector2(vector<int> v){
    for(int i=0; i<v.size(); i++)
        cout << v[i] << " ";
}

int main(){
//    creating vectors
    vector<int> v;
    vector<int> v1 = {1, 2, 3, 4, 5};
    vector<int> v2(10);
    vector<int> v3(6, 9);

//    inserting values, avg complexity: O(1)
    v.push_back(4);
    v.push_back(5);
    v.push_back(7);

    cout << "Array v: ";
    printVector(v);

    cout << "\nLast value: " << v.back();
    v.pop_back();
    cout << "\nLast value after pop: " << v.back();

    cout << "\nArray v1: ";
    printVector(v1);

    cout << "\nArray v2: ";
    printVector(v2);

    cout << "\nArray v3: ";
    printVector(v3);
}
