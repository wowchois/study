'''
heap 문제

TEST CASE

scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
[2,4] 12 -1
[6] 5 1
[4] 5 -1

1. list를 heap으로 처리한다.
2. heap에서 [0]을 가져오는건 제일 작은 값을 가져옴. K와 비교
3. heappop으로 첫번째 작은 수와 두번째 작은수를 pop한다.
4. 스코빌 계산 후 heap에 다시 push한다. (자동정렬)
'''

# 정확도 100 효율성 0 
# 원인 : while문에서 min(scoville) 으로 비교했기 때문

# 효율성 통과한 경우 1
# before : while min(scoville) < K:
# after  : while scoville[0] < K: 
    
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
  
    while scoville[0] < K:
        if len(scoville) == 1: return -1
    
        first_low = heapq.heappop(scoville)
        second_low = heapq.heappop(scoville)

        num = first_low + (second_low*2)

        heapq.heappush(scoville, num)
        answer += 1
    else:
        if len(scoville) == 1: return 1
    
    return answer





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
