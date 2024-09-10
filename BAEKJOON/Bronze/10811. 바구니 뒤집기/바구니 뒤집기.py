baskets = []

N, M = map(int, input().split(' '))

for a in range(N) :
    baskets.append(a+1)


for a in range(M) :
    i, j = map(int, input().split(' '))

    for b in range((j - i + 1) // 2) :
        tmp = baskets[i-1]
        baskets[i-1] = baskets[j-1]
        baskets[j-1] = tmp
        i += 1
        j -= 1
    # print(baskets)

for value in baskets :
    print(value, end=' ')