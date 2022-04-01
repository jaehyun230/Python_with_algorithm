n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range (n+1)]

for _ in range (m) :
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for a in range (n+1) :
  for b in range (n+1) :
    if a == b :
      graph[a][b] = 0

# k를들렸다가 x로 출발
x, k = map(int, input().split())

for k in range (n+1) :
  for a in range (n+1) :
    for b in range (n+1) :
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#시작이 1번
answer = graph[1][k] + graph[k][x]

if answer > INF :
  print(-1)
else :
  print(answer)
