N = int(input())
scores = list(map(int, input().split(' ')))
high_score = max(scores)
new_avg = 0

for i in scores :
    new_avg += i/high_score*100

print(new_avg/N)