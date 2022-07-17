'''
카카오 2020 인턴 level1
x,y 좌표 풀이

numbers	hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
'''



def getDist(xy1,xy2):
    return abs(xy1[0]-xy2[0]) + abs(xy1[1]-xy2[1]) 

def solution(numbers, hand):
    answer = ''
    coords = {1:[0,0],2:[0,1],3:[0,2]
             ,4:[1,0],5:[1,1],6:[1,2]
             ,7:[2,0],8:[2,1],9:[2,2]
             ,10:[3,0],0:[3,1],12:[3,2]}
    l_hand = 10
    r_hand = 12
    
    for n in numbers:
        if n in [1,4,7]:
            l_hand = n
            answer += 'L'
        elif n in [3,6,9]:
            r_hand = n
            answer += 'R'
        else:
            l_dist = getDist(coords[l_hand],coords[n])
            r_dist = getDist(coords[r_hand],coords[n])
            
            if (l_dist < r_dist) or (l_dist == r_dist and hand == 'left'):
                l_hand = n
                answer += 'L'
            elif (l_dist > r_dist) or (l_dist == r_dist and hand == 'right'):
                r_hand = n
                answer += 'R'

    
    return answer
