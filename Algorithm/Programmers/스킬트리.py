'''
TEST CASE

skill	skill_trees	return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
'''


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
