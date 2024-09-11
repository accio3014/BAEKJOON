T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    A,B = a,b
    while(a!=0):    # 최대 공약수 구하기
        b = b%a
        a,b = b,a   
        # print(a,b)
    gcd = b         # 최대 공약수
    
    print(A * B // b)