
'''


n	words	result
3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]

'''


from collections import deque

def solution(n, words):
    answer = [0,0]
    last_word = []
    turn = 1
    que = deque(words)
    
    while que:
        for i in range(n):
            w = que.popleft()
            if w in last_word or (last_word and last_word[-1][-1] != w[0]):
                answer = [i+1, turn]
                return answer
            last_word.append(w)
        turn += 1

    return answer
