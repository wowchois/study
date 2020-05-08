# Summer/Winter Coding(~2018)
# level 2. 영어 끝말잇기

def get_fn(n,i) :
    n1 = (i+1)//n
    n2 = (i+1)%n
    
    if n2 != 0 : n1 = n1+1
    elif n2 == 0 : n2 = n

    return [n2,n1]

def solution(n, words):
    answer = [0,0]

    for i in range(len(words)) :
        if i == 0 : continue
        if words[i-1][-1] != words[i][0] :
            answer = get_fn(n,i)
            break
        elif words[i] in words[:i] :
            answer = get_fn(n,i)
            break
    return answer