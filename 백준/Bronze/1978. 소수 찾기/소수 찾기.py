N = int(input())
num = list(map(int, input().split()))
result = 0

for i in num:
    for j in range(2, i+1): # 1은 소수가 아니기 때문에 2부터 반복 
        if(i % j == 0):     # 딱 나눠 떨어지는 경우
            if(i == j):     # 자기 자신으로 나눠 떨어지는 경우
                result +=1
            break

print(result)