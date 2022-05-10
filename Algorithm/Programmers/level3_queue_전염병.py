

# 효율 0
#어려운 부분 : 몇일에 걸쳐서 전염됬는지 count하는 부분
from collections import deque
def solution(m, n, infests, vaccinateds):
    answer = 0
    direct = [(0,1),(0,-1),(1,0),(-1,0)]
    left = []
    flue_cnt = 0
    
    if len(infests)+len(vaccinateds) == m*n: return answer

    while len(infests)+len(vaccinateds) != m*n:
        que = deque(infests)

        while que: 
            fy, fx = que.popleft()
            if [fy, fx] in left: continue

            for dy, dx in direct:
                ny = fy+dy
                nx = fx+dx
                if 0<ny<=m and 0<nx<=n and [ny,nx] not in vaccinateds and [ny,nx] not in infests:
                    flue_cnt += 1
                    left.append([fy, fx])
                    infests.append([ny, nx])
            if flue_cnt == 0:
                return -1
        answer += 1

    return answer
