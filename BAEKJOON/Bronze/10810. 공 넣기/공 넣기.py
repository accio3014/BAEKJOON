N, M = map(int, input().split())
basket = []

for i in range(N):
    basket.append(0)

for a in range(M):
    i, j, k = map(int, input().split())

    for b in range(i-1, j, 1):
        basket[b] = k

for c in basket:
    print(c, end=" ")