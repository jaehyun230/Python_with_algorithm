#이진 탐색 타겟팅 데이터
target = int(input())

#이진 탐색할 데이터리스트
data = list(map(int, input().split()))

def binary_search(target,start, end) :
  mid = (start + end) // 2
  if start > end :
    return -1
  if data[mid] == target :
    return mid + 1
  elif data[mid] > target :
    return binary_search(target, start, mid-1)
  else :
    return binary_search(target, mid+1, end)

answer = binary_search(target, 0, len(data)-1)

print(answer)
