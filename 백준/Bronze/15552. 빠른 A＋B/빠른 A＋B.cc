#include <iostream>
using namespace std;

int main() {
    int T = 0;
    
    // 아래 2줄 코드는 입력을 빠르게 해주는 코드, 자세한 사항은 검색 필요!
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    cin >> T;

    for(int i = 0; i < T; i++){
        int A, B = 0;

        cin >> A >> B;
        cout<<A+B<<"\n";
    }

	return 0;   
}