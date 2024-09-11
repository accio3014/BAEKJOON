# number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# rev_number = number[::-1]
# result = ''

# N, B = map(int, input().split())
# length = 0

# # 몇 자리 수인지 구하기
# a = 0
# while(True) :
#     if(N > B**a) :
#         length += 1
#     else :
#         break

# # print(length)

# for i in range(length) :
#     for j in rev_number :
#         num = number.index(j) * (B**i)
#         if(N >= num) :
#             N -= num
#             result += j
#             length -= 1
#             break

# print(result)


# 이 문제의 경우 이전 문제를 역산해서 풀게 되면 무조건 시간 초과를 하기 때문에 역산 이 아닌 다른 방식으로 접근 해야 함

number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''

N, B = map(int, input().split())

# N이 0이 될 때까지 반복, 진법 변환이 끝날 때 까지 반복
while(N > 0):
    result = number[N % B] + result # 나머지를 이용하여 진법 변환, 소인수 분해와 비슷하게 몇 자리인지 알 수 있음
    N //= B

print(result)