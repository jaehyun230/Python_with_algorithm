N = int(input())
array = list(map(int, input().split()))

M = int(input())
find_list = list(map(int, input().split()))

array.sort()

def binary_search(array, target) :
  start = 0
  end = len(array)-1
  
  while start <= end :
    mid = (start + end)//2
    if array[mid] == target :
      return True
    elif array[mid] > target :
      end = mid - 1
    else :
      start = mid + 1
      
  return False

for i in range (len(find_list)) :
  check = binary_search(array, find_list[i])
  if check == True :
    print("yes", end = '')
  else :
    print("no", end = '')
  if i != len(find_list) -1 :
    print(" ", end = '')
