whiteboard = []

for _ in range(100) :
    line = []
    for _ in range(100) :
        line.append(0)
    whiteboard.append(line)

N = int(input())

for _ in range(N) :
    x, y = map(int, input().split())
    for i in range(10) :
        for j in range(10) :
            whiteboard[x+i][y+j] = 1

count = 0
for row in whiteboard:
    count += row.count(1)

print(count)