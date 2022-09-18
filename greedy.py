# ------ 그리디 알고리즘 -------- #

# 매 상황에서 단순히 큰 값만 고르는 알고리즘 (최적의 해를 보장할 수 없다)

N = 1260
def greedy(N) :
  count = 0 
  while N // 500 > 0 : 
    N -= 500
    count += 1
  while N // 100 > 0 : 
    N -= 100
    count += 1 
  while N // 50 > 0:
    N -= 50
    count += 1 
  while N // 10 > 0:
    N -= 10
    count += 1
  return count 

def newgreedy(N) : 
  box = [500 , 100 , 50 , 10]
  count = 0 
  for num in box :
    while N // num > 0 : 
      N -= num
      count += 1 
  return count
  
newgreedy(N) 
