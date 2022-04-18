'''
TEST CASE

genres : ["classic", "pop", "classic", "classic", "pop"]	
plays : [500, 600, 150, 800, 2500]	

RESULT : [4, 1, 3, 0]

https://programmers.co.kr/learn/courses/30/lessons/42579
'''

def solution(genres, plays):
    answer = []
    length = len(genres)
    obj = {x : 0 for x in genres}
    
    for i in range(length) :
        obj[genres[i]] += plays[i]
    
    for q in obj :
        nowMax = max(obj.keys(),key=(lambda x:obj[x]))
        playsArr = [(j,plays[j]) for j in filter(lambda x:genres[x] == nowMax, range(length))]
        #for j in filter(lambda x:genres[x] == nowMax, range(length)) :
        #    playsArr.append((j,plays[j]))

        playsArr.sort(key=lambda x:x[1],reverse=True)
        obj[nowMax] = 0
        
        for k in playsArr[:2] :
            answer.append(k[0])
    
    return answer
