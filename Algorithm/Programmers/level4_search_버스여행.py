




# 31점 
import sys
sys.setrecursionlimit(10000)

def solution(n,signs):
    answer = []
    
    for i in range(n):
        answer.append(get_sign(n,i,signs,signs[i]))
    
    return answer

def get_sign(n,i,signs,answer):
    try:
        idx = signs[i].index(1)
    except:
        return answer
    
    if n < 1: return answer
    
    answer = [1 if x+y >= 1 else 0 for x,y in zip(answer,signs[idx])]
    return get_sign(n-1,idx,signs,answer)
    
