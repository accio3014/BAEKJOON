N, M = map(int, input().split())

A = []
B = []

for line in range(N*2) :
    row = list(map(int, input().split()))
    if(line < N) :
        A.append(row)
    else :
        B.append(row)


for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()