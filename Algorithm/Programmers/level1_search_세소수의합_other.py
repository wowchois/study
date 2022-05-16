'''
완전탐색 유형 

3개 조합 중 소수가 되는 값 count 

TEST CASE

nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4

'''


from itertools import combinations

def solution(nums):
    answer = -1
    comb = list(combinations(nums,3))
    answer = list(map(isTrue,map(sum,comb))).count(True)

    return answer

def isTrue(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False #소수아님
    return True #소수
