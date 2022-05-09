'''
Hash 유형

TEST CASE

dirs	answer
"ULURRDLLU"	7
"LULLLLLLU"	7
'''

'''
어려운 부분 : 
1. 방문한 점만 count했는데 현재와 이동할 좌표 모두 관리해야함
2. 한 길을 왕복으로 생각하면 2가지가 된다. (1->2 / 2->1 모두 같은 길이라 같이 생각해야한다.)
'''

#첫번째 풀이 (정확성 35점)
#문제점 : 한 길에 양방향 케이스를 고려해야 한다.
def solution(dirs):
    answer = 0
    direction = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    x, y = (0,0)
    now_stack = []
    move_stack = []
    
    for r in dirs:
        dx, dy = direction[r]
        sx, sy = x+dx, y+dy
        
        if -5 <= sx <= 5 and -5 <= sy <= 5:
            if (x, y) in now_stack and (sx, sy) in move_stack:
                continue
            now_stack.append((x, y))
            x, y = sx, sy
            move_stack.append((sx, sy))
    
    answer = len(now_stack)
    
    return answer


# 통과한 풀이 
# 양방향 고려해서 (현재 X, 현재 Y, 이동할 X, 이동할 Y) , (이동할 X, 이동할 Y, 현재 X, 현재 Y) 
# 모두 고려한 후 중복제거하고 /2 한다. 
def solution(dirs):
    answer = 0
    direction = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    x, y = (0,0)
    stack = []
    
    for r in dirs:
        dx, dy = direction[r]
        sx, sy = x+dx, y+dy
        
        if -5 <= sx <= 5 and -5 <= sy <= 5:
            stack.append((x, y, sx, sy))
            stack.append((sx, sy, x, y))
            x, y = sx, sy

    answer = len(set(stack)) // 2
    
    return answer
