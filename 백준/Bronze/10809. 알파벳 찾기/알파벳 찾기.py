S = input()
a = [-1] * 26
 
for i in range(len(S)):
    if(a[ord(S[i])-97] != -1):  # 아스키 코드를 이용하여 알파벳의 위치 찾기
        pass
    else:
        a[ord(S[i])-97] = i
        
print(*a)                       # *를 붙여 리스트의 값만 출력