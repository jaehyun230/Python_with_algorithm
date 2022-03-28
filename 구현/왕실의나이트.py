N = input()

x = int(N[1])
y = ord(N[0]) - 96

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]
answer = 0

for i in range (len(dx)) :
  nx = x + dx[i]
  ny = y + dy[i]
  if nx > 0 and nx < 9 and ny > 0 and ny < 9 :
    answer +=1

print(answer)
