'''
TEST CASE

s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
'''

def solution(s):
    cnt = 0
    
    for (i,v) in enumerate(s) :
        if i == 0 and v == ')' : return False
        elif cnt < 0 : return False
        else :
            if v == '(' :
                cnt += 1
            else :
                cnt -= 1
            
    if cnt != 0 :
        return False

    return True
