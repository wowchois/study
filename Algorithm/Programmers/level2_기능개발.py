'''
TEST CASE

progresses	speeds	return
[93,30,55]	[1,30,5]	[2,1]

'''


# deque 사용
from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    day = [math.ceil((100-p)/s) for p,s in zip(progresses,speeds)]
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
    cnt = 1
    
    for p,s in zip(progresses[1:],speeds[1:]) :
        d = math.ceil((100 - p)/s)
        if max_d < d : 
            answer.append(cnt)
            cnt = 1
            max_d = d
        else :
            cnt += 1
    answer.append(cnt)
    
    return answer
  
