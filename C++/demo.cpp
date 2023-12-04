#include <iostream>
using namespace std;

int main() {
    int k;
    cin >> k;
    if (k % 2 == 0 && k/2 %2 == 0) cout << "YES";
    else cout << "NO";
    return 0;
}