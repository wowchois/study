'''
TEST CASE

healths	items	return
[200,120,150]	[[30,100],[500,30],[100,400]]	[1,2]
[300,200,500]	[[1000, 600], [400, 500], [300, 100]]	[3]
'''

# 63.6 점 (효율성 0)
def solution(healths, items):
    answer = []
    
    for idx,item in enumerate(items):
        else_h = 0
        for h in healths:
            if else_h < h-item[1]:
                else_h = h-item[1]
    
        if else_h >= 100:
            answer.append(idx+1)
    
    return answer


# 통과
from collections import deque
from heapq import heappush,heappop

# 체력 작은순서대로 두고, 체력소모 적은게 체력적은 상대에 해당되면 pop
def solution(healths, items):
    answer = []
    healths.sort()
    item = [[x[0],x[1],i] for i,x in enumerate(items)]
    item.sort(key=lambda x:x[1])
    que = deque(item)
    heap = [] #사용한아이템
    
    for h in healths:
        while que:
            attack,use,idx = que[0]
            if h-use < 100: 
                break
            else:
                que.popleft()
                heappush(heap,[-attack,idx+1])
        if heap:
            _, i = heappop(heap)
            answer.append(i)
    
    answer.sort()    
    return answer
