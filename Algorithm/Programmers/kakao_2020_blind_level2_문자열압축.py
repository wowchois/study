'''
https://programmers.co.kr/learn/courses/30/lessons/60057

TEST CASE

s / result
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17
'''


# 첫번째 풀었을때
def solution(s):
    answer = 0
    loopLen = len(s)//2
    resultArr = []
    
    if loopLen < 1 : #문자열 길이 1인 경우
        return len(s)
    
    for i in range(1,loopLen+1) :
        n = 1
        result = ''
        for j in range(0,len(s),i) :
            #print(i,j,s[j:j+i],s[j+i:j+i+i])
            if s[j:j+i] == s[j+i:j+i+i] :
                n += 1
            else :
                if n > 1 :
                    result += str(n)
                n = 1
                result += s[j:j+i]
        resultArr.append(len(result))
            
    #print(resultArr)
    answer = min(resultArr)
    
    return answer




# 두번쨰 풀었을떄
def solution(s):
    answer = 0
    result = []
    length = len(s)
    
    if length == 1 : return length

    for n in range(1,(length//2)+1) :
        cnt = 1
        txt = ''
        for t in range(0,length,n) :
            if s[t:t+n] == s[t+n:t+n+n] :
                cnt += 1
            else :
                if cnt > 1 :
                    txt += str(cnt)+s[t:t+n]
                else :
                    txt += s[t:t+n]
                cnt = 1
        else :
            result.append(len(txt))      
    
    return min(result)







