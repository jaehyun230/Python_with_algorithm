N = int(input())
array = set(map(int, input().split()))

M = int(input())
find_list = list(map(int, input().split()))

for i in range (len(find_list)) :
  
  if find_list[i] in array :
    print("yes", end = '')
  else :
    print("no", end = '')
  if i != len(find_list) -1 :
    print(" ", end = '')
