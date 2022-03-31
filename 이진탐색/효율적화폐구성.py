n, m = map(int, input().split())

#최대 화폐가치보다 높은 가치로 초기화
d = [10001] * (m+1)
money = []
for i in range(n) :
  money.append(int(input()))

d[0] = 0

#다이나믹 프로그래밍 보텀업 방식 진행
for i in range(n) :
  for j in range(money[i], m+1) :
    if d[j-money[i]] != 10001 : # (i - k)원을 만드는 방법이 존재할 경우
      d[j] = min(d[j], d[j-money[i]] + 1)

if d[m] == 10001 :
  print(-1)
else :
  print(d[m])
