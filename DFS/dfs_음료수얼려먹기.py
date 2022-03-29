n, m = map(int, input().split())

graph = []

def dfs(x,y) :
  if x < 0 or x >= n or y < 0 or y >= m :
    return
  if graph[x][y] == 0 :
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
  return

for i in range (n) :
  data = list(map(int, input()))
  graph.append(data)

#print(graph)
  
answer = 0
for i in range(n) :
  for j in range(m) :
    if graph[i][j] == 0 :
      dfs(i,j)
      answer +=1

print(answer)
