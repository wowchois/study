
'''
완전탐색 - 재귀 유형

TEST CASE

n	result
2	[ [1,2], [1,3], [2,3] ]

'''

#import sys
#sys.setrecursionlimit(10000)

def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer

# t1 : 출발, t2 : 환승, t3 : 도착
# 0. n == 1이 되면 t3로 이동하고 종료
# 1. n-1개는 모두 t2로 이동 (t3 환승)
# 2. 마지막 n은 t3로 이동
# 3. t2의 n-1개 모두 t3로 이동 (t1 환승)
def hanoi(n, t1, t2, t3, answer):
    if n == 1: # 0.
        answer.append([t1, t3])
        return
    hanoi(n-1, t1, t3, t2, answer)  # 1.
    answer.append([t1, t3])         # 2. 
    hanoi(n-1, t2, t1, t3, answer)  # 3.

