'''
완전탐색 유형

TEST CASE

m	weights	return
3000	[500, 1500, 2500, 1000, 2000]	3
3000	[500, 1500, 2500, 1000, 2000, 3000]	4

'''


from itertools import combinations

def solution(m, weights):
    answer = 1 if m in weights else 0  # 대상인 m이 리스트에 있는 경우 미리 +1 한다.
    min_arr = [x for x in weights if x < m]  # m보다 큰 값은 미리 제거한다. (더해서 m이 되어야 해서)
    
    for i in range(2, len(min_arr)):
        te = [1 for c in list(combinations(min_arr, i)) if sum(c) == m]
        answer += len(te)
    
    return answer
