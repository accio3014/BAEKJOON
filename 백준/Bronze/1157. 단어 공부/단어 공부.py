word = input().upper()                    # 입력받은 문자를 대문자로 저장
word_list = list(set(word))               # 중복 문자를 제외하고 리스트로 알파벳 하나씩 저장
cnt = []                                  # 문자 개수를 저장할 리스트 생성

for i in word_list:                         
    check = word.count(i)                 # 문자에서 알파벳의 수를 저장
    cnt.append(check)                     # 저장된 알파벳의 수를 리스트에 추가

if(cnt.count(max(cnt)) >= 2):             # 리스트의 최대값이 2개 이상인 경우
    print('?')
else:
    print(word_list[cnt.index(max(cnt))]) # 최대값의 인덱스 번호를 기반으로 리스트에서 출력