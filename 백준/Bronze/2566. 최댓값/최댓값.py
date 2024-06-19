table = []
maximum = -1        # -1을 한 이유는 0~100 사이의 값이기 때문에 0을 한 경우 2차원 리스트가 전부 0인 경우 위치를 잡지 못함
maximum_row = 0
maximum_col = 0

for i in range(9) :
    row = list(map(int, input().split()))
    table.append(row)
    if(maximum < max(row)) :
        maximum = max(row)
        maximum_row = i + 1
        maximum_col = (row.index(maximum)) + 1

print(maximum)
print(maximum_row, maximum_col)