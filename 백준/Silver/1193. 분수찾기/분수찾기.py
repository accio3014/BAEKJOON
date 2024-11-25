X = int(input())

# 라인수의 끝 값은 1, 3, 6, 10, 15, 21... triangular number이기 때문에 이것을 사용하여 몇 번째 라인인지 계산
# triangular number : n(n+1)/2
n = 1
triangular_number = 1

while(X > triangular_number) :
    n += 1
    triangular_number = n * (n + 1) / 2

# print(n)

# 몇 번째 숫자인지 판단하기 위해 이전 제일 마지막 숫자를 X에서 빼면 됨
last_triangular_number = (n-1) * ((n-1) + 1) // 2
index = X - last_triangular_number
# print(index)


if(n % 2 == 0) :
    a = index
    b = n - index + 1
else:
    a = n - index + 1
    b = index

print("%d/%d" % (a, b))