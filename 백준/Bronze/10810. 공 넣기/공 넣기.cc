#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N, M = 0;
    int basket[101] = {0};              // 0으로 array를 초기화 안하면 오류 발생, 이상한 값이 들어감

    cin >> N >> M;

    for(int a = 1; a <= M ; a++){
        int i, j, k = 0;

        cin >> i >> j >> k;             // 값 입력
        for(int b = i; b <= j; b++){    // i부터 j까지 k의 값을 넣음
            basket[b] = k;              // 값을 덮어쓰기 때문에 자연스럽게 바구니에는 값이 1개만 들어감
        }

        // Check
        // cout << "Basket : ";
        // for(int i = 1; i <= N; i++){
        //     cout << basket[i] << " ";
        // }
        // cout << endl << endl;
    }

    for(int i = 1; i <= N; i++){
        cout << basket[i] << " ";
    }

	return 0;   
}
