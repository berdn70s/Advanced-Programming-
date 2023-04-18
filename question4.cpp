#include <iostream>
#include <cmath>
using namespace std;
//question 4
double sum_of_equation(int n) {
     if (n == 0) {
        return 0;
    }

     return sum_of_equation(n-1) + pow(-1, n+1) / n;
}

int main() {
     int n;
    cout << "Enter the value of n: ";
    cin >> n;

     double result = sum_of_equation(n);
    cout << "The sum of the given equation is: " << result << endl;

    return 0;
}
