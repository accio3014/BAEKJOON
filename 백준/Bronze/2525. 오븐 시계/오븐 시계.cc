#include <iostream>
using namespace std;

int main() {
    int A, B, C = 0;
    int plus = 0;

    cin >> A >> B;
    cin >> C;

    B = B + C;
    plus = B / 60;
    B = B % 60;
    A = A + plus;

    if(A > 23){
        cout << A-24 << " " << B << endl;
    } else{
        cout << A << " " << B << endl;
    }
    
    return 0;
}