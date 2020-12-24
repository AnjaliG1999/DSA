#include <bits/stdc++.h>
using namespace std;

int firstRepeated (int arr[], int n) {
    int minIndex = -1;
    map<int, bool> elements;
    for(int i=n-1; i>-1; i--){
        if (elements.find(arr[i]) != elements.end())
            minIndex = i;
        else
            elements.insert(pair<int, bool>(arr[i], true));
    }
    return minIndex;
}

int main(){
    int arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10};
    int n = sizeof(arr)/ sizeof(arr[0]);

    int firstIndex = firstRepeated(arr, n);
    int first = arr[firstIndex];

    if(firstIndex != -1)
        cout << "The first repeating element is " << first << " at index " << firstIndex;
    else
        cout << "There are no repeating elements";
}