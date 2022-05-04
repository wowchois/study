'''
Queue 문제

TEST CASE

progresses	speeds	return
[93,30,55]	[1,30,5]	[2,1]

1. 100-진행사항 = 남은작업 / speeds 한 결과를 올림처리한다.
2. 첫번째 값을 max로 두고 비교하면서 처리.
앞의 최대 작업시간보다 크면 따로 배포해야되서 answer에 추가,
앞의 최대 작업보다 작거나 같으면 같이 배포해야되서 +1
'''


# deque 사용
from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    day = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    que = deque(day)
    cnt = 1
    max_d = que.popleft()
    
    for _ in range(len(day)-1) :
        d = que.popleft()
        if max_d >= d :
            cnt += 1
        else :
            answer.append(cnt)
            cnt = 1
            max_d = d
    answer.append(cnt)
    
    return answer

  
# deque 사용 안한 경우
import math
def solution(progresses, speeds):
    answer = []
    max_d = math.ceil((100 - progresses[0])/speeds[0])
    cnt = 0
    
    for p,s in zip(progresses[1:],speeds[1:]) :
        d = math.ceil((100 - p)/s)
        if max_d < d : 
            answer.append(cnt)
            cnt = 0
            max_d = d
        cnt += 1
    answer.append(cnt)
    
    return answer
  
