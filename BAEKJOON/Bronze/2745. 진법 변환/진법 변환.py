number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0

N, B = input().split()
length = len(N) - 1

for i in N :
    result += number.index(i) * (int(B) ** length)
    length -= 1
print(result)