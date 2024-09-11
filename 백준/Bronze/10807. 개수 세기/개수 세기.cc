#include <iostream>
using namespace std;

int main() {

    int N, v, count = 0;
    
    cin >> N;
    int numbers[N];

    for(int i = 0; i < N; i ++){
        cin >> numbers[i];
    }

    cin >> v;

    for(int i = 0; i < sizeof(numbers)/sizeof(*numbers); i ++){
        if(v == numbers[i]){
            count += 1;
        }
    }

    cout<<count;

	return 0;   
}