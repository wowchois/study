'''

TEST CASE
v	result
[[1, 4], [3, 4], [3, 10]]	[1, 10]
[[1, 1], [2, 2], [1, 2]]	[2, 1]
'''

'''
1. X,Y 따로 counter로 개수 확인
2. 개수 1개인 좌표 출력
'''
from collections import Counter

def solution(v):
    answer = []
    x_list = Counter([x for x,y in v])
    y_list = Counter([y for x,y in v])
    
    for key,cnt in x_list.items():
        if cnt == 1 : answer.append(key)
    
    for key,cnt in y_list.items():
        if cnt == 1 : answer.append(key)
        
    return answer
