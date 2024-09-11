X=int(input())

line=1
while(X>line):      # 몇 번째 라인인지를 판단
    X -= line
    line+=1

# print(line)
# print(X)

if(line%2==0):      # 짝수 라인인 경우
    a=X
    b=line-X+1
else:               # 홀수 라인인 경우
    a=line-X+1
    b=X
    
print('%d/%d' % (a, b))