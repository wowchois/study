import heapq

def solution(scv, K):
    answer = 0
    scv.sort()
    
    while scv[0] < K :
        if len(scv) == 1 :
            return -1
        else :
            s1 = heapq.heappop(scv)
            s2 = heapq.heappop(scv)
            cal = s1 + (s2 * 2)
            heapq.heappush(scv,cal)
            answer += 1
    
    return answer
