#include <iostream>
using namespace std;

int main() {
    int A, B, C = 0;

    cin >> A >> B >> C;

    if(A != B && B != C && A != C) {
		int m = 0;

		m = max(A, max(B, C));
		cout << m * 100;
	} else if (A == B && A == C) {
		cout << 10000 + A * 1000;
	} else if (A == B || A == C) {
		cout << 1000 + A * 100;
	} else {
		cout << 1000 + B * 100;
	}
	return 0;   
}