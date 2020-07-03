# 11279번 최대 힙
#125772KB 256ms


import heapq #최소 힙 모듈
#import sys

N = int(input()) #int(sys.stdin.readline())
result = []

for i in range(N) : 
  x = int(input()) #int(sys.stdin.readline())

  if x != 0 :
    heapq.heappush(result, (-x)) # 최소 힙 모듈을 최대 힙으로 사용하기 위해 음수 변경
  else : 
    if not result : 
      print(0)
    else : 
      print(heapq.heappop(result) * -1)