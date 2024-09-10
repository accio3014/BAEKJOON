#include <iostream>
using namespace std;

int main() {
    int X, N = 0;
    
    cin >> X;
    cin >> N;

    for(int i = 0; i < N; i++){
        int a, b = 0;
        cin >> a >> b;

        X = X - (a * b);
    }

    if(X == 0){
        cout << "Yes";
    } else {
        cout << "No";
    }
    
	return 0;   
}