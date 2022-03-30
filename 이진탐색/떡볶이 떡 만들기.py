n, m = map(int, input().split())
data = list(map(int, input().split()))

def binary_search(data, start, end, m) :
  max_len = 0
  while start <= end :
    sum = 0
    mid = (start+end)// 2

    for i in data :
      if i > mid :
        sum += i - mid
    if sum >= m :
      max_len = max(max_len, mid)
      start = mid + 1

    elif sum < m :
      end = mid - 1

  return max_len
      
answer = binary_search(data, 0, max(data), m)
print(answer)
