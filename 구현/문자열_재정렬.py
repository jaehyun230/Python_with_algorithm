data = list(input())
answer = ""
sum = 0
for i in range(len(data)) :
  if data[i].isalpha() :
    answer +=data[i]
  else :
    sum +=int(data[i])

answer.sort()
answer +=str(sum)

print(answer)
