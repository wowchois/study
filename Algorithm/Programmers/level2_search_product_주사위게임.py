'''
완전탐색 - product

TEST CASE
monster	S1	S2	S3	result
[4,9,5,8]	2	3	4	500
[4,9,5,8]	2	3	3	555

몬스터를 만나지 않을 확률 구하기

product : 두개 이상의 리스트에서 조합을 구할 때 사용
'''


from itertools import product

def solution(monster, S1, S2, S3):
    answer = -1
    s1_list = [s for s in range(1,S1+1)]
    s2_list = [s for s in range(1,S2+1)]
    s3_list = [s for s in range(1,S3+1)]
    
    all_list = [s1_list] + [s2_list] + [s3_list]
    prd_list = list(product(*all_list))
    result = [1 for x in prd_list if sum(x)+1 in monster] #몬스터 만날 확률
    
    answer = int((1 - (len(result) / len(prd_list))) * 1000)
    
    return answer
