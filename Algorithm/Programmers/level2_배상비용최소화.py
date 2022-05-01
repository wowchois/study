'''
TEST CASE

N	works	result
4	[4,3,3]	12
2	[3,3,3]	17
15 [4,4,4] 0
'''

# 효율성/정확성 통과
def solution(no, works):
    result = 0
    idx = 0
    if no > sum(works): return 0

    while no > 0:
        works.sort(reverse=True)
        min_n = works[-1]
        
        if works[0] > min_n:
            works[0] -= 1
        else:
            works[idx] -= 1
            idx = idx+1 if idx < len(works)-1 else 0
        no -= 1
    
    result = sum([x**2 for x in works])

    return result

