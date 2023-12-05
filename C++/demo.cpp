#include <iostream>
#include <string>
using namespace std;

string abbreviate(string word) {
    int length = word.length();
    if (length > 10) {
        return word[0] + to_strinwg(length - 2) + word[length - 1];
    } else {
        return word;
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
        cout << abbreviate(word) << endl;
    }
    return 0;
}