N = int(input())
data = list(input().split())
x = y = 1

for i in data:
  if i == 'R' :
    if y < N :
      y +=1
  elif i == 'L' :
    if y > 1 :
      y -=1
  elif i == 'U' :
    if x > 1 :
      x -=1
  elif i == 'D' :
    if x < N :
      x +=1
    
print(x, y)
