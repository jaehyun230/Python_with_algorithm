n = int(input())

number = []

for i in range (n) :
  data = int(input())
  number.append(data)

number.sort(reverse=True)

for i in number :
  print(i, end =' ')
