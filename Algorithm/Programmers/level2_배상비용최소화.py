'''
heap 문제

TEST CASE

N	works	result
4	[4,3,3]	12
2	[3,3,3]	17
15 [4,4,4] 0

1. 일할 시간이(no) 총 일의 양보다 크면 배상비용은 0
2. 최대힙으로 처리하기 위해서 (-)처리
3. heapreplace = pop -> push 순으로 실행

- heap은 O(log n) 이지만, sort는 O(n log n) 이라서 heap이 더 빠르다. (n배 차이) 
'''

# heap 사용
import heapq

def solution(no, works):
    if no > sum(works): return 0

    result = 0
    works = [-x for x in works]
    heapq.heapify(works)

    for _ in range(no):
        heapq.heapreplace(works,works[0]+1)
    
    result = sum([x**2 for x in works])

    return result



# sort 사용 - 효율성/정확성 통과
def solution(no, works):
    result = 0
    idx = 0
    if no > sum(works): return result

    for _ in range(no):
        works.sort(reverse=True)
        min_n = works[-1]
        
        if works[0] > min_n:
            works[0] -= 1
        else:
            works[idx] -= 1
            idx = idx+1 if idx < len(works)-1 else 0
    
    result = sum([x**2 for x in works])

    return result


# sort사용 - 코드 개선
def solution(no, works):
    result = 0
    idx = 0
    if no > sum(works): return result

    for _ in range(no):
        works.sort()
        works[-1] -= 1
    
    result = sum([x**2 for x in works])

    return result
