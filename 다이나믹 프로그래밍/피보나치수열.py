# N 번째 피보나치 값
N = int(input())

d = [0] * 101

d[1] = 1
d[2] = 1

for i in range (3, N+1) :
  d[i] = d[i-1] + d[i-2]

print(d[N])
