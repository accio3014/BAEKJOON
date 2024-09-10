word = []

for _ in range(5) :
    line = list(input())
    word.append(line)

for i in range(15) :
    for j in range(5) :
        try :
            print(word[j][i], end='')
        except :
            continue