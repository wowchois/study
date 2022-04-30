'''
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
[2,4] 12 -1
[6] 5 1
[4] 5 -1
'''

# 정확도 100 효율성 0
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
  
    while min(scoville) < K:
        if len(scoville) == 1: return -1
    
        first_low = heapq.heappop(scoville)
        second_low = heapq.heappop(scoville)

        num = first_low + (second_low*2)

        heapq.heappush(scoville, num)
        answer += 1
    else:
        if len(scoville) == 1: return 1
    
    return answer
