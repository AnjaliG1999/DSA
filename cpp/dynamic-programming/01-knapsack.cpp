#include <bits/stdc++.h>

using namespace std;

int knapsack(int wt[], int val[], int W, int n){
    if (W == 0 || n == 0) return 0;
    
    if(wt[n-1] <= W) {
        return max(knapsack(wt, val, W, n-1), val[n-1] + knapsack(wt, val, W-wt[n-1], n-1));
    } 
    return knapsack(wt, val, W, n-1);
}

int table[4][51];

int knapsackMemoized(int wt[], int val[], int W, int n){
    if(W == 0 || n == 0) {
        return 0;
    }
    
    if(table[n][W] != -1) return table[n][W];
    
    if(wt[n-1] <= W) {
       return table[n][W] = max(knapsackMemoized(wt, val, W, n-1), val[n-1] + knapsackMemoized(wt, val, W-wt[n-1], n-1));
    } 
    return table[n][W] = knapsackMemoized(wt, val, W, n-1);
}

int knapsackTopDown(int wt[], int val[], int W, int n){
    for(int i=0; i<=n; i++){
        for(int j=0; j<=W; j++){
            if(i==0 || j==0){
                table[i][j] = 0;
            } else {
                if(wt[i-1] <= j){
                    table[i][j] = max(table[i-1][j], val[i-1] + table[i-1][j-wt[i-1]]);
                } else table[i][j] = table[i-1][j];
            }
        }
    }
    return table[n][W];
}

int main()
{
    int wt[] = {10, 20, 30};
    int val[] = {60, 100, 120};
    int W = 50;
    int n = sizeof(wt)/sizeof(wt[0]);
    
    memset(table, -1, sizeof(table));
    
    // int profit = knapsack(wt, val, W, n);
    // int profit = knapsackMemoized(wt, val, W, n);
    int profit = knapsackTopDown(wt, val, W, n);
    cout << "Maximum profit: " << profit;
}