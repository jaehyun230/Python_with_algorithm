a,b = map(int, input().split())

matrix = []

for i in range (a) :
  data = list(map(int, input().split()))
  min_value = min(data)
  matrix.append(min_value)

print(max(matrix))
