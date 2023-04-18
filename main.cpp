#include <iostream>
#include <cmath>
using namespace std;

double result = 0;

void recursive_function(int n) {
    // base case
    if (n == 0) {
        return;
    }

    recursive_function(n-1);

    result += pow(-1, n+1) / n;
}

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;

    recursive_function(n);

    cout << "The sum of the given equation for the range of k from 1 to " << n << " is: " << result << endl;

    return 0;
}
