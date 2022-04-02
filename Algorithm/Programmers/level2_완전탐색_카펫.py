'''
세로 1,2 는 안됨 -> 가운데 들어갈게 없음.
target 약수로 계산

식 : 가로*2 + (세로-2) * 2 = brown개수
'''

def solution(brown, yellow):
    answer = []
    target = brown + yellow
    
    for i in range(3,int(target**(1/2)) + 1) :
        if target % i == 0 :
            w = target // i
            if (w*2) + ((i-2)*2) == brown :
                answer.append(w)
                answer.append(i)
                break
    
    return answer
