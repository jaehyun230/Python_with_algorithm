N = int(input())
array = [0] * 1000001

data = input().split()
for i in data :
  array[int(i)] = 1

M = int(input())
find_list = list(map(int, input().split()))

for i in range (len(find_list)) :
  
  if array[find_list[i]] == 1 :
    print("yes", end = '')
  else :
    print("no", end = '')
  if i != len(find_list) -1 :
    print(" ", end = '')
