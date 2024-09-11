N, K = map(int, input().split())
measure = [0]

for i in range(1, N+1, 1) :
    if((N % i) == 0) :
        measure.append(i)

try :
    print(measure[K])
except :
    print(measure[0])