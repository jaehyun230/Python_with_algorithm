import sys
input = sys.stdin.readline
INF = int(1e9) # 10억값을 무한값으로 생각하며 지정

#노드, 간선의 개수 입력받기
n, m = map(int, input().split())
#시작 노드 번호
start = int(input())
#노드 연결되어있는 정보 리스트
graph = [[] for i in range(n+1)]
#방문 체크 리스트
visited = [False] * (n+1)
#거리 테이블 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for _ in range(m) :
  #a 번노드에서 b번노드로 갈떄 c비용
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

#방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드 번호 반환
def get_smallest_node() :
  min_value = INF
  index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i] :
      min_value = distance[i]
      index = i
  return index

def dijkstra(start) :
  #시작 노드 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start] :
    distance[j[0]] = j[1]

  for i in range (n-1) :
  #현재 최단 거리가 가장 짧은 노드 꺼내 방문 처리
    now = get_smallest_node()
    visited[now] = True
    #  현재 노드와 연결된 다른 노드 확인
    for j in graph[now] :
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]] :
        distance[j[0]] = cost

#최단경로 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1) :
  # 도답할 수 없는 경우, 무한이라고 출력
  if distance[i] == INF :
    print("INFINITY")
  # 도달할 수 있는 경우 거리 출력
  else :
    print(distance[i])
