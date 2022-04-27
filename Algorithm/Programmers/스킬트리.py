'''
TEST CASE

skill	skill_trees	return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
'''


# SUCCESS CODE
# skill에 포함안되면 continue
# skill에 포함되는데 조건에 해당되어도 continue
# skill에 포함되는데 조건에 해당안되면 break
# deque 의 popleft 는 O(1) 시간복잡도

from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for txt in skill_trees :
        s_que = deque(skill)
        for a in txt :
            if a in skill and a != s_que.popleft() : break
        else : answer += 1
            
    return answer



# FAIL CODE
def solution(skill, skill_trees):
    answer = 0
    before = 0
    
    for s in skill_trees :
        before = 0
        cnt = 0
        for v in skill :
            f = s.find(v)
            if cnt == 0 and f == -1 : break
            if (before <= f and before != -1) or f == -1 :
                cnt += 1
                before = f
            elif before == -1 and f > -1 : 
                break
            else : break
            if cnt == len(skill) : 
                answer += 1
           
    return answer

