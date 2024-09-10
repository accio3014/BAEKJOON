A, B, C = map(int, input().split())

if(B >= C):                         # 제품 가격보다 재료비가 많이 들면 이익이 불가능
    print(-1)
else:
    print(int(A // (C-B)+1))        # 이익이 발생하기 위해서는 고정 비용에서 제품 가격 - 가변 비용 +1을 한 후 고정 비용을 나눠줘야 한다.