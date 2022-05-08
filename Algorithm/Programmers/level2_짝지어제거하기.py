'''

TEST CASE

s	result
baabaa	1
cdcd	0
cc 1
bcaacb 1
bcaccaab 0
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
    
    answer = 1 if len(stack) == 0 else 0
    
    return answer
