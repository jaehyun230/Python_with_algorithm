import math

def is_prime_number(x) :
  
  #2부터 (x-1)까지 모두 확인
  for i in range(2, int(math.sqrt(x)) + 1):
    # x가 i로 나누어 떨어지면 소수가 아님
    if x % i == 0 :
      return False
    # 나누어 떨어지지않음으로 소수임
    else :
      return True
