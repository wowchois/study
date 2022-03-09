import heapq

def solution(scv, K):
    answer = 0
    scv.sort()
    
    while scv[0] < K :
        if len(scv) == 1 :
            flag = True
            if scv[0] >= K :
                return answer
            else :
                return -1
        else :
            cal = scv[0] + (scv[1] * 2)
            scv = scv[2:]
            scv.append(cal)
            answer += 1
            break
            
        if len([x for x in scv if x >= 7]) == len(scv) :
            flag = True
            return answer
    
    
    return answer
