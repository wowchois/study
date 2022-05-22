

'''
동적계획법 dynamic programming 유형

n	result
4	5
5 8

'''


# 점화식 : f(n) = f(n-1) + f(n-2)

from collections import deque

def solution(n):
    answer = 0
    fn = deque([0,1]) # 1개 경우는 이미 포함하고 시작
    
    for i in range(1,n):
        fn.append(fn[1] + fn[0])
        fn.popleft()
    
    answer = sum(fn) % 1000000007
    
    return answer
