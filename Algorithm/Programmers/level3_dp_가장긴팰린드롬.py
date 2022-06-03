'''
동적계획법 유형

TEST CASE
s	answer
"abcdcba"	7
"abacde"	3
'''

# 0부터 끝자리->0까지 줄여가면서 일치 찾는다.
# 일치하면 시작지점 1증가
# 종료지점도 1증가 후 현재지점부터 문자전체길이까지 시작지점과 일치하는지 탐색
def solution(s):
    length = len(s)
    
    if length < 2: return length
    
    for l in range(length,0,-1):
        start = 0
        end = l - 1
        while end < length:
            if check_equal(s,start,end):
                return l
            start += 1
            end += 1

    return 1

# 다를때까지 탐색, 양쪽 모두 같으면 팰린드롬 조건
def check_equal(s, start, end):
    for i in range(((end - start) // 2) + 1):
        if s[start + i] != s[end - i]:
            return False
    return True

