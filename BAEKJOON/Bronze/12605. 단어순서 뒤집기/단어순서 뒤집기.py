N = int(input())

for i in range(N):
  data = list(input().split())
  data.reverse()
  print("Case #%d: " % (i+1) , end="")
  for j in range(len(data)):
    print(data[j], end=" ")
  print()