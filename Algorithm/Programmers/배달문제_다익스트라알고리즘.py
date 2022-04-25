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
            #print(que)

    print(que)

    re = [x for x in que if x <= K]
    #print(len(re))

    return len(re)
