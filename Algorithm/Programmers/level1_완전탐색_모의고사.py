def solution(answers):
    result = []
    size = len(answers)
    n = [0,0,0]
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    p1 = (n1*(size//len(n1)))+n1[:size%len(n1)]
    p2 = (n2*(size//len(n2)))+n2[:size%len(n2)]
    p3 = (n3*(size//len(n3)))+n3[:size%len(n3)]
    
    for i in range(size) :
        if answers[i] == p1[i] :
            n[0] += 1
        if answers[i] == p2[i] :
            n[1] += 1
        if answers[i] == p3[i] :
            n[2] += 1
    
    result = [x+1 for x,val in enumerate(n) if val >= max(n)]
    
    return result
