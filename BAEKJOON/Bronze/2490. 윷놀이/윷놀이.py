for i in range(3):
  A, B, C, D = map(int, input().split())

  data = [A, B, C, D]
  count = 0
  for i in range(len(data)):
    if(0 == data[i]):
      count += 1

  if(count == 0):
    print("E")
  elif(count == 1):
    print("A")
  elif(count == 2):
    print("B")
  elif(count == 3):
    print("C")
  elif(count == 4):
    print("D")