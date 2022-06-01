
'''
동적계획법 유형

TEST CASE

m	n	puddles	return
4	3	[[2, 2]]	4
'''

#좌표로 배열 관리해서 지나온 길은 이전길과 더하는 방식으로 진행
#양방향 이동은 아니며, 아래와 오른쪽 이동만 생각
#웅덩이는 구분하기 위해 -1 로 처리하며, 웅덩이 만나면 0으로 변경 
# (이미 웅덩이를 만나서 다른곳으로 이동하기 때문에 0으로 변경해서 계산값을 유지한다. -1이면 왔던길 다시 되돌아가는 거라서)

def solution(m, n, puddles):
    coord = [[0]*(m+1) for _ in range(n+1)] #좌표계산쉽게 1부터 시작
    coord[1][1] = 1
    
    for x,y in puddles: #웅덩이 -1대입
        coord[y][x] = -1
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if coord[y][x] == -1: #웅덩이만날경우
                coord[y][x] = 0
                continue
            coord[y][x] += (coord[y][x-1] + coord[y-1][x]) % 1000000007
            #      왼쪽값(오른쪽 이동 이전값) + 위의값(아래 이동 이전값) 더한값 
            # => 결과적으로 오른쪽과 아래로 이동한 경로 모두 더한값을 구해야 해서
    
    return coord[n][m]
