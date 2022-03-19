"""
의상들을 입을 수 있고 안입을 수 있어서 +1,
의상을 안걸치는 경우는 없기에 -1

(의상1의 수+1) * (의상2의 수+1) ... -1

"""


def solution(clothes):
    answer = 1
    key = {x[1] : 0 for x in clothes}
    
    for c in clothes :
        key[c[1]] += 1
    
    for n in key.values() :
        answer *= (n+1)
    
    return answer-1
