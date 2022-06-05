
'''
동적계획법 유형

TEST CASE
words	result
["go","gone","guild"]	7
["abc","def","ghi","jklm"]	4
["word","war","warrior","world"]	15
'''

def solution(words):
    answer = 0
    trie = set_trie(words) #단어 트리 만들기

    for word in words:
        w_map = trie
        for idx,val in enumerate(word):
            if w_map[val][0] <= 1:
                break
            
            w_map = w_map[val][1]
        answer += idx + 1
    
    return answer

# 단어 trie 만들기
def set_trie(words):
    root = {}
    
    for word in words:
        w_map = root
        for c in word:
            w_map.setdefault(c,[0,{}])
            w_map[c][0] += 1
            w_map = w_map[c][1]
    return root
  
