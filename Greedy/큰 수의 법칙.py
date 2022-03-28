a,b,c = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse=True)

answer = 0
count = 0
while b != 0 :
  if count == c :
    answer +=data[1]
    count = 0
  else :
    answer +=data[0]
    count +=1
  b -=1

print(answer)
