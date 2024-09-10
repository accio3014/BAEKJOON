def fibonacci(num) :
    if(num <= 1):       # n이 0일 떄는 0, 1일 때는 1이므로 n<=1을 조건으로 검
        return num
    return fibonacci(num-1) + fibonacci(num-2)

n = int(input())
print(fibonacci(n))