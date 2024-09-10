S = input()
a = [0] * 26

for i in S:
    a[ord(i)-97] += 1   # 아스키 코드를 이용

print(*a)               # *를 붙여 리스트의 값만 출력