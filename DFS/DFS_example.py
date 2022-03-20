def dfs(graph, v, visited) :
  #현재 노드 방문처리
  visited[v] = True
  print(v, end=' ')
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visitied)
      
#각 노드 연결된 정보 (2차원 리스트)      
graph = [
  []
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

#각노드 방문정보 그래프 초기화
visitied = [False] * 9

#dfs 호출
dfs(graph, 1, visited)
  
