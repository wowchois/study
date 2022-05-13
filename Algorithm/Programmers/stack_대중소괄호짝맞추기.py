'''
Stack 유형

TEST CASE

s	answer
"{{}}"	true
"({})[]"	true
"[)"	false
"]()["	false
"([())]"	false
'''

# ord() 문자를 숫자로 변경하는데, 여는괄호는 닫는괄호보다 작으며, 둘이 차이는 1,2 정도 차이다.
def solution(s):
    stack = []
    
    for t in s:
        if stack and 0 < ord(t) - ord(stack[-1]) <= 2:
            stack.pop()
        else:
            stack.append(t)
        
    return stack == []
