### 한지점에서 다른 특정 지점 까지 최단경로가 아닌 모든 지점에서 모든 지점까지 최단경로를 모두 구해야 하는 경우
INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력 받기
n = int(input())
m = int(input())

#2 차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화

graph = [[INF] * (n+1) for _ in range (n+1)]

#자기 자신에서 자기 자신으로 가는 비용 초기화
for a in range(1, n+1) :
  for b in range(1, n+1) :
    if a == b :
      graph[a][b] = 0

#각 간선에 대한 정보 입력, 그 값으로 초기화

for _ in range (m) :
  #a에서 b로 가는 비용을 c로 초기화
  a,b,c = map(int, input().split())
  graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) :
  for a in range(1, n+1) :
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] +graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1) :
  for b in range(1, n+1) :
    # 연결되지 않은경우
    if graph[a][b] == INF :
      print("INFINITY", end = " ")
    #연결된 경우
    else :
      print(graph[a][b], end= " ")
  print()
