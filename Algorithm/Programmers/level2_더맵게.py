'''
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
[2,4] 12 -1
[6] 5 1
[4] 5 -1
'''

# 정확도 100 효율성 0 
# 원인 : while문에서 min(scoville) 으로 비교했기 때문,,
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



# 효율성 통과한 경우 1
while min(scoville) < K:    # before
while scoville[0] < K:      # after


# 효율성 통과한 경우 2 - 정확도 떨어짐 ([6] 5 1 케이스 통과못함)
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
  
    while scoville[0] < K:
        try:
            first_low = heapq.heappop(scoville)
            second_low = heapq.heappop(scoville)
            heapq.heappush(scoville, first_low + (second_low*2))
        except:
            return -1
        answer += 1
    
    return answer
