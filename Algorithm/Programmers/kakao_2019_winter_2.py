# Level 2 - 튜플

#s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
#s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
#s = "{{20,111},{111}}"
#s = "{{123}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):
    stack = []; answer = []
    s = s[2:-2]
    s = s.replace('},','/').replace('{','')    
    s_list = [list(map(int,n.split(','))) for n in s.split('/')]
    
    for i in range(len(s_list)) :
        for j in range(len(s_list)) :
            if len(s_list[j]) == i+1 :
                for s in s_list[j] :
                    if s not in answer : answer.append(s)
    
    return answer


solution(s)