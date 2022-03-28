N = int(input())
data = list(input().split())
x = y = 1
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
move_type = ['U', 'D', 'L', 'R']

for i in data:
  for j in range (len(move_type)) :
    if i == move_type[j] :
      nx = x + dx[j]
      ny = y + dy[j]
      if 0 < nx < N and 0 < ny < N :
        x = nx
        y = ny
    
print(x, y)
