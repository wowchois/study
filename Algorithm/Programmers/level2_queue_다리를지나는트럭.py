'''
1. queue가 0인 경우 트럭 추가
2. queue가 다리길이보다 작은 경우 (queue가 전부 채워지지 않은 상태)
    : queue합이 weight보다 크면 0으로 채우고, 아니면 트럭 추가
3. queue가 모두 채워진 경우
    : 맨 앞 queue를 pop시킨다.
4. 반복 이후, 마지막 트럭까지 queue에 진입 한 경우
    : 반복문 종료하고 다리길이만큼 트럭이 전진할 예정으로, 총 시간 + 다리길이로 계산
'''


import queue

def solution(bridge_length, weight, tw):
    answer = 0
    cnt = 0
    qsum = 0
    que = queue.Queue()     

    while cnt < len(tw) :
        if que.qsize() == 0 :
            que.put(tw[cnt])
            qsum += tw[cnt]
            cnt += 1
            answer += 1
        elif que.qsize() < bridge_length :
            if qsum + tw[cnt] > weight :
                que.put(0)
            else :
                que.put(tw[cnt])
                qsum += tw[cnt]
                cnt += 1
            answer += 1
        elif que.qsize() == bridge_length :
            poll = que.get()
            qsum -= poll
        #print(answer, qsum)
    
    return answer+bridge_length
