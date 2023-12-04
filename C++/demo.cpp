#include <iostream>
using namespace std;

int main() {
    int k,n=1;
    cin >> k;
    double s=0;
    while (s <= k) {
        s += 1.0/n;
        n++;
    }
    cout << n-1;
        return 0;
}