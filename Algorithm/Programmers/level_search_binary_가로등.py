

'''
이진탐색 유형

TEST CASE
l	v	output
15	[15,5,3,7,9,14,0]	3
5	[2,5]	2
'''

# 80점 
def solution(l, _v):
    answer = 0
    _v.sort()
    v = _v[:]
    v.append(0)
    v.append(l)
    v = list(set(v))
    v.sort()
    
    start = v[0]
    max_calc = 0

    for i in range(1,len(v)):
        t = v[i] - start
        max_calc = t if max_calc < t else max_calc
        start = v[i]

    if len(_v) == 1 or max_calc + _v[-1] <= l:
        answer = max_calc 
    else: 
        answer = (max_calc // 2) + (max_calc % 2)

    return answer
