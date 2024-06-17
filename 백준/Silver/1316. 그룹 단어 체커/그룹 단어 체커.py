N = int(input())
count = N

for i in range(N):
    word = input()
    for index in range(len(word) - 1):            # 단어의 처음부터 비교, -1을 한 이유는 현재 위치와 다음 위치를 비교할 예정
        if(word[index] != word[index + 1]):       # 현재위치의 알파벳과 다음 위치의 알파펫이 다를 경우 = 그룹단어인 경우, 같은 경우도 그룹이기 때문에 굳이 조건으로 만들지 않음
            if(word[index + 1] in word[:index]):  # 다음 위치의 알파벳이 현재위치 이전에 알파벳에 있을 경우, 즉 그룹단어가 아님
                count -= 1
                break
print(count)