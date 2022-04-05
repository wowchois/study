
def solution(number, k):
    answer = ''
    length = len(number)
    loop = length - k
    delete = 0
    nIdx = 0

    while delete != k :
        for i in range(len(number)) :
            if i+1 == len(number) : break
            if number[i] < number[i+1] :
                number = number.replace(number[i],'',1)
                delete += 1
                break
            else :
                nIdx += 1
        if nIdx >= loop and len(number) == length :
            return number[:loop]
    
    return number
