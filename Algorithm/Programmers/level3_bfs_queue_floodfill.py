'''
BFS DFS 유형 - queue로 풀기

TEST CASE

n	m	images	정답
2	3	[[1, 2, 3], [3, 2, 1]]	5
3	2	[[1, 2], [1, 2], [4, 5]]	4

1. 상하좌우 방향변수 설정
2. 방문한 값은 대체하고 n,m 만큼 방문할 때 대체값이면 건너뛰기
3. 타겟의 x,y와 방향변수 x,y 를 더해서 상하좌우 조건에 해당되며, 값이 같으면 queue에 추가하고 방문한값 대체
4. queue의 값 = 찾은 x,y 값 으로 또 같은 값이 있는지 상하좌우로 찾으면서 반복 (3반복)
5. 더이상 상하좌우에 같은값이 없으면 popleft해서 queue에 값이 없으므로 while 종료
'''


rom collections import deque

def solution(n, m, image):
    answer = 0
    direct = [(0,1),(0,-1),(1,0),(-1,0)] #방향변수
    
    for y in range(n):
        for x in range(m):
            #방문한 값은 대체
            if image[y][x] == float('inf'):
                continue
            targret = image[y][x]
            que = deque([(y,x)]) 
            
            #같은 수 없을때까지 찾기 
            #-> 같은 수 que에 넣고 그 수의 x,y로 다시 방향변수로 같은 수 찾기 
            while que: 
                ny, nx = que.popleft()
                
                for dy, dx in direct: 
                    py = ny+dy
                    px = nx+dx
                    if -1<py<n and -1<px<m and targret==image[py][px]:
                        image[py][px] = float('inf')
                        que.append((py,px))
            answer += 1 
                
    return answer
