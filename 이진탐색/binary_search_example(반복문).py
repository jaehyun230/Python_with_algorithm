#이진 탐색 타겟팅 데이터
target = int(input())

#이진 탐색할 데이터리스트
data = list(map(int, input().split()))

def binary_search(target) :
  start = 0
  end = len(data)-1
  
  while start <=end :
    mid = (start+end)//2
    if data[mid] == target :
      return mid
    elif data[mid] > target :
      end = mid -1
    else :
      start = mid + 1
  # 타겟팅 데이터 없을경우
  return -1

#1번째부터 시작 시 +1 (카운트 0부터작시 +1 제거)
print(binary_search(target)+1)
    
