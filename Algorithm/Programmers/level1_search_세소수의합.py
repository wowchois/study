'''
완전탐색 유형?

TEST CASE

n	return
33	4
9	0

'''

# 어려운부분 : 소수 3개 더하는부분
# 해결 : combinations = 리스트의 모든 조합 구하는 라이브러리

from itertools import combinations

def solution(n):
    n_arr = [True] * (n+1) #인덱스 0부터 n+1까지 True (소수 시작은 2부터 n까지 필요)

    #에라토스테네스 : 소수 구하는 방법 중 하나
    for i in range(2, int(n**0.5)+1): #n의 최대약수 = n**0.5 = sqrt(n) 까지만 체크하면됨.
        if n_arr[i]:
            for j in range(i+i,n+1,i): # i의 다음 배수(i+i)부터 i의 배수 false (2+2,n+1,2) -> 4부터 2씩 건너뛰기 
                n_arr[j] = False
    
    idx_arr = [i for i in range(2,len(n_arr)) if n_arr[i] == True]
    combi = [sum(x) for x in list(combinations(idx_arr,3))].count()
    
    return combi
