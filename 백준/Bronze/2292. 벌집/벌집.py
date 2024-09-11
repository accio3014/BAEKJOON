N = int(input())

house = 1               # 벌집, 1부터 시작
count = 1               # 거리, 1부터 시작
while(N > house):       
    house += 6 * count
    count += 1

print(count)