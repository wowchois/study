'''

동적프로그래밍 - 다익스트라 알고리즘
: 모든정점까지 최단경로 구하는 알고리즘 - 범위 넓은 그래프에서도 사용하지만, 음수가 있는경우 사용못한다.
- 1번 노드부터 시작한다고 하면, 5개 노드 까지 거리 구함.
- 1번 노드에서 가장 가까운 노트 찾기
- 가장 가까운 노드2에서 다른 노드까지 경로 구하고 현재 노드와 1번노드 거리까지 더한다. (1-2거리 + 2-다른노드거리 = 1-다른노드까지 거리)
- 반복

TEST CASE

N	road	K	result
5	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	3	4
6	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	4	4
'''

# 내 풀이
def solution(N, road, K):
    answer = 0
    que = [999] * N
    que[0] = 0

    for root in range(1,N+1) :
        for r in road :
            if root == r[0] :
                #print(root,r)
                #print('---',que[r[1]-1],r[2],que[root-1])
                if que[r[1]-1] > r[2] + que[root-1] :
                        que[r[1]-1] = r[2] + que[root-1]
            elif root == r[1] :
                if que[r[0]-1] > r[2] + que[root-1] :
                        que[r[0]-1] = r[2] + que[root-1]
   
    re = [x for x in que if x <= K]
    #print(len(re))

    return len(re)




# 다른 풀이
from queue import PriorityQueue # 파이썬 내장 모듈

def dijkstra(road, N):
    queue = PriorityQueue() # 우선순위 큐
    queue.put([1, 0]) # 1번 마을부터 시작
    
    dist = [float('inf')] * (N + 1) # 계산하기 편하게 N+1 길이만큼 리스트 생성
    dist[1] = 0 # 1번 마을은 무조건 거리가 0
    
    while not queue.empty():
        current, current_cost = queue.get() # 현재 선택된 노드와 비용
        for src, dest, cost in road: # 출발지, 목적지, 비용
            next_cost = cost + current_cost # 비용
            if src == current and next_cost < dist[dest]:
                # src가 현재 선택된 노드면서 목적지까지 더 저렴할 경우
                dist[dest] = next_cost # 최소 비용을 갱신
                queue.put([dest, next_cost]) # Priority Queue에 추가
            elif dest == current and next_cost < dist[src]:
                # dest가 현재 선택된 노드면서 출발지까지 더 저렴할 경우
                dist[src] = next_cost # 최소 비용을 갱신
                queue.put([src, next_cost]) # Priority Queue에 추가
    return dist

def solution(N, road, K):
    dist = dijkstra(road, N)
    return len([x for x in dist if x <= K]) # list comprehension


