def solution(n, lost, reserve):
    answer = 0
    cnt = 0
    
    for j in range(len(lost)) : #여벌 있고 도난당한 경우
        if lost[j] in reserve :
            cnt += 1
            reserve[reserve.index(lost[j])] = '*'
            lost[j] = '*'
    
    for i in lost :
        if i == '*' : continue
        if i-1 in reserve :
            cnt += 1
            reserve[reserve.index(i-1)] = '-'
        elif i+1 in reserve :
            cnt += 1
            reserve[reserve.index(i+1)] = '-'
    
    answer = n - len(lost) + cnt
            
    return answer