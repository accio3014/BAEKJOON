#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <random>
#include <chrono>

using namespace std;

int main() {
    int N = 0;
    double average = 0;

    cin >> N;
    vector<int> scores(N);

    // 값 입력
    for(int i = 0; i < N; i++) {
        int score = 0;
        cin >> score;
        scores[i] = score;
    }

    // 최대값 구하기
    double max = *max_element(scores.begin(), scores.end());

    for(int i = 0; i < N; i++) {
        average = average + double(scores[i])/max*100;
    }

    average = double(average / N);
    cout << average << endl;
    

    return 0;
}