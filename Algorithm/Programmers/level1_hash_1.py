#해시 - 완주하지 못한 선수
#case 1. 효율성out
def solution(participant, completion):
    answer = ''
    
    for c in completion :
        participant[participant.index(c)] = ''
    
    answer = ''.join(participant)
    return answer


#case 2. counter 이용
from collections import Counter

def solution(participant, completion):
    answer = ''
    
    p = Counter(participant)
    c = Counter(completion)
    answer = list((p-c).keys())[0]
    
    return answer

#case 3. hash 이용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer