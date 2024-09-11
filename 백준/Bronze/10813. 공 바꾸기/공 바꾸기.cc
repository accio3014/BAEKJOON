#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N, M = 0;
    int number = 1;
    int basket[101] = {0};              // 0으로 array를 초기화 안하면 오류 발생, 이상한 값이 들어감

    cin >> N >> M;

    
    // 바구니를 번호로 채움
    for(int idx = 1; idx <= N; idx++){
        basket[idx] = number;
        number++;
    }

    for(int a = 1; a <= M ; a++){
        int i, j, tmp = 0;

        cin >> i >> j;             // 값 입력
        
        tmp = basket[i];
        basket[i] = basket[j];
        basket[j] = tmp;
        

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