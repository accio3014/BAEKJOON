while(True):
  word = list(input())
  if(word == ['0']):
    break
  else:
    if(list(reversed(word)) == word):
      print('yes')
    else:
      print('no')