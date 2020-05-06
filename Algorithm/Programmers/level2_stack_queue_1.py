#level 2
#stack/queue - 탑

def solution(heights):
    answer = [0] * len(heights)

    for i in range(len(heights)-1,-1,-1) :
        arr = heights[:i]
        for j in range(len(arr)-1,-1,-1) : 
            if heights[i] < arr[j] :
                answer[i] = j+1
                break
    return answer