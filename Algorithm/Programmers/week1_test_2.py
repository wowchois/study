'''
TEST CASE - 최솟값 구하기 (배상비용최소화 문제와 비슷)

works	n	result
[4, 3, 3]	4	12
[2, 1, 2]	1	6
[1,1]	3	0
'''

# heap으로 푼 경우 - 효율성 통과
import heapq

def solution(n, works):
    answer = 0
    if n > sum(works): return answer

    heap=[]
    for w in works:
        heapq.heappush(heap,-w)

    for _ in range(n):
        w = heapq.heappop(heap)
        heapq.heappush(heap,w+1)
    answer = sum([x**2 for x in heap])

    return answer
  
  
 # 정렬로 푼 경우 - 효율 0
def solution(n, works):
    answer = 0
    if n > sum(works): return answer

    for _ in range(n):
        works.sort()
        works[-1] -= 1
    answer = sum([x**2 for x in works])
    
    return answer
  
  
