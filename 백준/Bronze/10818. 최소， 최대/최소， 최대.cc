#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N = 0;

    cin >> N;
    int numbers[N];

    for(int i = 0; i < N; i++){
        cin >> numbers[i];          // array에 데이터 넣기
    }

    sort(numbers, numbers + N);     // numbers array 정렬, array의 길이만큼 +

    cout << numbers[0] << " " << numbers[N-1] << endl;

	return 0;   
}