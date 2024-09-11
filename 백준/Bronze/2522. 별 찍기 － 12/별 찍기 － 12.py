# 한번에 출력하는 것이 아닌 상단 하단으로 나눈 후 각각 출력
N = int(input())

for i in range(1, N + 1, 1):
    print(' ' * (N - i), end="")
    print('*' * i)

for i in range(1, N, 1):
    print(' ' * i, end="")
    print('*' * ( N - i))