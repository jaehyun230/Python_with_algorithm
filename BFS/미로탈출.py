from collections import deque

n, m = map(int, input().split())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y) :
  queue = deque()
  queue.append((x, y))

  while queue :
    a,b = queue.popleft()
    for i in range (len(dx)) :
      nx = a+dx[i]
      ny = b+dy[i]
      if nx >=0 and nx < n and ny >=0 and ny < m :
        if graph[nx][ny] == 1 :
          graph[nx][ny] = graph[a][b] + 1
          queue.append((nx, ny))
  
  return graph[n-1][m-1]
    

for i in range (n) :
  data = list(map(int, input()))
  graph.append(data)

answer = bfs(0,0)
print(answer)
