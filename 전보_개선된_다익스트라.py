import heapq

#도시 수, 연결 간선 수, 도움 알림 지점
n, m, k = map(int, input().split())
INF = int(1e9)
graph = [[] for i in range (n+1)]

distance = [INF] * (n+1)

for _ in range (m) :
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


def dijkstra(start) :
  q = []
  #시작노드 출발 코스트 0으로 초기화 시작
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q :
    dist, now = heapq.heappop(q)
    if distance[now] < dist :
      continue
    for i in graph[now] :
      cost = i[1] + dist
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(k)

net = []
for i in range (1, n+1) :
  if distance[i] == INF :
    continue
  
  else :
    net.append(distance[i])

#시작노드 제외, 제일 cost 오래걸리는 값
print(len(net)-1, max(net))

    
