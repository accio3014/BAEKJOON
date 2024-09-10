#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int students[31] = {0};
    int number = 1;
    
    // 학생인원 넣기
    for(int i = 1; i <= 30; i++){
        students[i] = number;
        number++;
    }

    for(int j = 0; j < 28; j++){
        int student = 0;

        cin >> student;
        students[student] = 0;
    }

    for(int k = 1; k <= 30; k++){
        if(students[k] != 0){
            cout << students[k] << endl;
        }
    }

	return 0;   
}