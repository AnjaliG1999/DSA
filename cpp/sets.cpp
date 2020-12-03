#include <bits/stdc++.h>
using namespace std;

void printSet(set<int> s){
    for(auto val: s)
        cout << val << " ";
}

void printSet(multiset<int> s){
    for(auto val: s)
        cout << val << " ";
}

int main(){
    set<int> s;
    set<int> s1 = {1, 2, 3, 4, 2};
    s.insert(5);
    s.insert(3);
    s.insert(9);

    cout << "Set s: ";
    printSet(s);

    cout << "\nSet s1: ";
    printSet(s1);

    int val = 2;
    cout << "\nNo. of " << val << "s in s1: " << s1.count(val) << "\n";

    multiset<int> s2 = {1, 2, 3, 4, 2, 2};
    cout << "Multiset s2: ";
    printSet(s2);
    cout << "\nNo. of " << val << "s in s2: " << s2.count(val);

    cout << "\n\n(Erase only one instance)\nMultiset s2: ";
    s2.erase(s2.find(val));
    printSet(s2);
    cout << "\nNo. of " << val << "s in s2: " << s2.count(val);

    cout << "\n\n(Erase all instances)\nMultiset s2: ";
    s2.erase(val);
    printSet(s2);
    cout << "\nNo. of " << val << "s in s2: " << s2.count(val) << "\n";
}
