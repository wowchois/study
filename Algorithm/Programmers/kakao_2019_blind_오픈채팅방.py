'''
TEST CASE

INPUT : ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
RESULT : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

https://programmers.co.kr/learn/courses/30/lessons/42888
'''


def solution(record):
    answer = []
    spArr = [x.split() for x in record]
    nameDict = {}
    
    for i in spArr :
        if i[0] != 'Leave' :
            nameDict[i[1]] = i[2]
    
    for j in spArr :
        if j[0] == 'Change' :
            continue        
        txt = '{0}님이 '.format(nameDict[j[1]])
        if j[0] == 'Enter' : txt += '들어왔습니다.'
        elif j[0] == 'Leave' : txt += '나갔습니다.'
        answer.append(txt)
    
    return answer
