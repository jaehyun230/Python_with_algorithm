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
    graph[a][b] = 1
    for i in range(len(dx)) :
      nx = a + dx[i]
      ny = b + dy[i]
      if nx >= 0 and nx < n and ny >=0 and ny <m :
        if graph[nx][ny] == 0 :
          queue.append((nx, ny))
            
for i in range (n) :
  data = list(map(int, input()))
  graph.append(data)

answer = 0

for i in range (n) :
  for j in range (m) :
    if graph[i][j] == 0 :
      bfs(i, j)
      answer +=1
      
print(answer)
