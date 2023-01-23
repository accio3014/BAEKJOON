A, B = map(list, input().split())

A.reverse()
B.reverse()
a = ''
b = ''
for i in range(len(A)):
  a += ''.join(A[i])
  b += ''.join(B[i])

if(int(a) > int(b)):
  print(a)
else:
  print(b)