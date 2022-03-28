n, m = map(int, input().split())
#d -> 바라보는 방향
x, y, d = map(int, input().split())

game_map = []
visit = [[0] * m for i in range (n)]

#북 서 남 동 (이동)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left() :
  global d
  if d == 0 :
    d = 3
  else :
    d -=1

for i in range (n) :
  data = list(map(int, input().split()))
  game_map.append(data)

answer = 1
turn_count = 0

while True :
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]

  if game_map[nx][ny] == 0 and visit[nx][ny] == 0 :
    visit[nx][ny] = 1
    x, y = nx, ny
    turn_count = 0
    answer +=1
    
  else :
    turn_count +=1

  if turn_count == 4 :
    nx = x -dx[d]
    ny = y -dy[d]

    if visit[nx][ny] == 0 :
      x = nx
      y = ny
    else :
      break
    turn_count = 0

print(answer)
