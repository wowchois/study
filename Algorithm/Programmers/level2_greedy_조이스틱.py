

def solution(name):
    answer = 0
    if set(name) == {'A'} : return 0
    
    for (idx,val) in enumerate(name) :
        answer += min(ord(val) - ord('A'), ord('Z') - ord(val))
    
    
    return answer
