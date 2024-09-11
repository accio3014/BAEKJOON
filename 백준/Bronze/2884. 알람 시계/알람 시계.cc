#include <iostream>
using namespace std;

int main() {
    int H, M = 0;

    cin >> H >> M;

    if(M < 45) {
        M = M + 15;
        H = H - 1;

        if(H < 0){
            H = 23;
        }
    } else {
        M = M - 45;
    }

    cout << H << " " << M << endl;
    
    return 0;
}