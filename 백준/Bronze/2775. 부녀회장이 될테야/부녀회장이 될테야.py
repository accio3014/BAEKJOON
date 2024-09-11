C = int(input())    # 테스트 케이스

for i in range(C):
    floor = int(input())    # 층
    room = int(input())     # 호수

    base = [i for i in range(1, room + 1)]  # 0층 부분 초기화

    # print(base)

    # 각층에 대한 리스트를 다시 생성
    for j in range(floor):
        for k in range(1, room):    # 각 층별 인원수 중 0번째 인덱스는 항상 1이기 때문에 1부터 반복

            base[k] += base[k-1]
        # print(base)
    
    print(base[room-1])