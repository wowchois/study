
'''
완전탐색 - bfs 유형

n	signs	answer
3	[[0,1,0],[0,0,1],[1,0,0]]	[[1,1,1],[1,1,1],[1,1,1]]
3	[[0,0,1],[0,0,1],[0,1,0]]	[[0,1,1],[0,1,1],[0,1,1]]

'''

# 1. 0번째부터 1인 index 찾는다.
# 2. 해당 1의 index들을 queue에 추가 (= 0번째 row가 가는 정류장들)
# 3. 가야할 정류장들을 하나씩 빼서 다음 갈 정류장을 찾는다.
# 4. 다음 가야 할 정류장에서 1을 찾으면 또 가야할 정류장이 있으므로 queue에 추가하고 들른 정류장은 1로 변경

from collections import deque

def solution(n,signs):
    
    for start in range(n):
        que = deque([idx for idx, val in enumerate(signs[start]) if val])

        while que:
            stop = que.popleft()
            
            for end, val in enumerate(signs[stop]):
                if val and signs[start][end] == 0:
                    signs[start][end] = 1
                    que.append(end)
    
    return signs
  
    

# 플로이드 워셜 방법
def solution(n,signs):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if signs[i][k] == 1 and signs[k][j] == 1:
                    signs[i][j] = 1
  
    return signs
  
  
# 재귀 - 31점 
import sys
sys.setrecursionlimit(10000)

def solution(n,signs):
    answer = []
    
    for i in range(n):
        answer.append(get_sign(n,i,signs,signs[i]))
    
    return answer

def get_sign(n,i,signs,answer):
    try:
        idx = signs[i].index(1)
    except:
        return answer
    
    if n < 1: return answer
    
    answer = [1 if x+y >= 1 else 0 for x,y in zip(answer,signs[idx])]
    return get_sign(n-1,idx,signs,answer)
    

  
