
#case 1. 효율성 통과 전

def solution(prices):
    answer = [0] * len(prices)

    for idx in range(len(prices)):
        cnt = -1
        for n in prices[idx:] :
            cnt+=1
            if prices[idx] > n : break
        answer[idx] = cnt

    return answer


#case 2. 효율성 통과 후

def solution(prices):
    length = len(prices)
    answer = [0] * length

    for idx in range(length):
        for num in range(idx+1,length) :
            answer[idx] += 1
            if prices[idx] > prices[num] : break

    return answer

'''
두 코드의 차이점
1. len() 에 접근하는 부분을 변수로 선언해서 접근수를 줄임.
2. cnt변수로 계산하지않고 answer에 직접 접근.
3. 두개의 for문 모두 range()로 index로 처리.
'''

