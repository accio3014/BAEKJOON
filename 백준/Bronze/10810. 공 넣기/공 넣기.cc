#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N, M = 0;
    int basket[101] = {0};

    cin >> N >> M;

    for(int a = 1; a <= M ; a++){
        int i, j, k = 0;

        cin >> i >> j >> k;
        for(int b = i; b <= j; b++){
            basket[b] = k;
        }
    }

    for(int i = 1; i <= N; i++){
        cout << basket[i] << " ";
    }

	return 0;   
}