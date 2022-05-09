'''
Stack & Hash 유형

TEST CASE
max_weight	specs	names	return
300	[["toy","70"], ["snack", "200"]]	["toy", "snack", "snack"]	2
200	[["toy","70"], ["snack", "200"]]	["toy", "snack", "toy"]	3

'''

# 놓쳤었던 부분 : allSum = weight 
# MAX보다 높은 짐은 1개를 더하고 그 트럭 무게 자체를 유지해야 다음 짐과 더할 수 있다.
from collections import deque

def solution(max_weight, specs, names):
    answer = 1
    specs_dict = dict(specs)
    que = deque(names)
    all_sum = int(specs_dict[que.popleft()])
    
    while que:
        name = que.popleft()
        weight = int(specs_dict[name])
        allSum += weight
        if allSum > max_weight: 
            allSum = weight
            answer += 1
         
    return answer
