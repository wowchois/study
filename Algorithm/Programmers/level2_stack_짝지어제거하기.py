'''
stack 유형

TEST CASE

s	result
baabaa	1
cdcd	0
cc 1
bcaacb 1
bcaccaab 0
'''

'''
1. 문자열 길이가 2이하인 케이스 미리 제거
2. 대상 문자열과 stack 비교하면서 값 같으면 pop 다르면 append
'''
def solution(s):
    answer = 0
    stack = []
    
    if len(s) < 2: return 0    
    if len(s) == 2: return 1 if s[0] == s[1] else 0

    for txt in s:
        if len(stack) == 0:
            stack.append(txt)
        else:
            if txt == stack[-1]:
                stack.pop()
            else:
                stack.append(txt)
    
    #answer = 1 if len(stack) == 0 else 0
    #return answer
    #코드 개선
    return int(stack == [])
