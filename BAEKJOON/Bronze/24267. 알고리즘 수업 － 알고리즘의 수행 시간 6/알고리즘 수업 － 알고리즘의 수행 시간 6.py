n = int(input())

n2 = n-2
sum = 0

for i in range(1, n-1):
    sum += n2 * i
    n2 -= 1

print(sum)
print(3)