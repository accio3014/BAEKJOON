#include <iostream>
using namespace std;

int main() {

    for(;;){
        int A, B = 0;
        
        cin >> A >> B;
        if(cin.eof() == true) {
           break;
        }
        cout << A + B << endl;
    }

	return 0;   
}