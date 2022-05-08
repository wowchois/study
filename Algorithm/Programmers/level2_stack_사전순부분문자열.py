'''
stack 유형

TEST CASE
s	result
"xyb"	"yb"
"yxyc"	"yyc"
"abz" "z"
'''

'''
1. stack 비어있으면 stack append
2. stack에 비교대상 있으면 현재대상(alpha) 와 비교해서 alpha가 더 작으면 그냥 append
alpha가 더 크면 마지막 요소를 제거 (큰요소가 나올때까지 반복 - 반복하다가 stack 비워지면 stack에 append하는 부분으로 넘어감(while 종료))

ex : 
yxyc []
xyc [y] -> x y 비교 : x 더 작아서 append, stack = [y,x]
yc [y,x] -> y x 비교 : x 더 작아서 pop, y는 append stack = [y,y]
c [y,y] -> c y 비교 : c 더 작아서 append, stack = [y,y,c]
'''
def solution(s):
    if len(s) == 1: return s
    answer = ''
    stack = []
    
    for alpha in s:
        while stack and stack[-1] < alpha:
            stack.pop()
        stack.append(alpha)
    
    answer = ''.join(stack)
    
    return answer
