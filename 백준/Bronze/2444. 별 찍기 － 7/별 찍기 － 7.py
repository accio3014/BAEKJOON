lines = int(input())

for i in range(1, lines*2, 1):
    if(i <= lines):
        for j in range(0, lines-i, 1):
            print(' ', end='')
        for j in range(0, 2*i-1, 1):
            print('*', end='')
        print()
    else:
        for j in range(i-lines):
            print(' ', end='')
        for j in range((2*lines-i)*2-1):
            print('*', end='')
        print()