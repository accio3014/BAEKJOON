C = int(input())

for i in range(C):
    H, W, N = map(int, input().split())

    floor = N % H                       # 배정 받는 방의 층
    room = (N // H) + 1            # 배정 받는 방의 호수
    if(floor == 0):
        floor = H
        room -= 1

    print(floor * 100 + room)