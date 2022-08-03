#level 1 
#정렬 - K번쨰 수
def solution(array, commands):
    answer = []
    
    for arr in commands :
        i = arr[0]; j = arr[1]; k = arr[2]
        li = array[i-1:j]
        li.sort()
        answer.append(li[k-1])
    
    return answer
