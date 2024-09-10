#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int numbers[9] = {0};
    int b[9] = {0};

    for(int i = 0; i < 9; i++){
        int number = 0;
        cin >> number;

        numbers[i] = number;
        b[i] = number;
    }

    sort(b, b + 9);
    cout << b[9-1] << endl;
    
    int test = b[9-1];
    int idx = 1;
    for(int j = 0; j < sizeof(numbers)/sizeof(*numbers); j++){
        if(test == numbers[j]){
            cout << idx << endl;
        }
        idx++;
    }

	return 0;   
}