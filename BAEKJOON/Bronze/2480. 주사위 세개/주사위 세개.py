A, B, C= map(int, input().split())
num = [A, B, C]
if(A == B == C):
    print(10000+A*1000)
elif(A == B):
    print(1000+A*100)
elif(A == C):
    print(1000+A*100)
elif(B == C):
    print(1000+C*100)
else:
    print(max(num)*100)
