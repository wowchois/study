
#case 1.
def solution(prices):
    answer = [0] * len(prices)

    for idx in range(len(prices)):
        cnt = -1
        for n in prices[idx:] :
            cnt+=1
            if prices[idx] > n : break
        answer[idx] = cnt

    return answer

