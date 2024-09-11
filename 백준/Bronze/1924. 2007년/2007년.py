# [풀이 방법]
# 일수를 모두 더한 후 7로 나누어 계산

x, y = map(int, input().split())

# 요일 및 월의 일수에 대한 정보를 리스트로 저장
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

today = 0

for i in range(x-1):
  today += month[i]

today = (today + y) % 7

print(week[today])