'''

동적프로그래밍 - 다익스트라 알고리즘

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
