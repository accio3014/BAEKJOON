nums = []
N = int(input())


while(N > 0):
    num = int(input())
    nums.append(num)

    N -= 1

nums.sort()

for i in nums:
    print(i)