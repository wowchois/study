
'''
정렬 유형

TEST CASE

d	budget	result
[1,3,2,5,4]	9	3
[2,2,3,3]	10	4

'''



# 풀이 1 - 더한 경우
def solution(d, budget):
    answer = 0
    sum_d = 0
    d.sort()
    
    for i in d:
        sum_d += i
        answer += 1 if sum_d <= budget else 0
    
    return answer

  
# 풀이 2 - 예산에서 뺀 경우 
def solution(d, budget):
  answer = 0
  d.sort()

  for i in d:
      if i <= budget:
          budget -= i
          answer += 1

  return answer
