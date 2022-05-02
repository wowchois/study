

# 63.6 점 (효율성 0)
def solution(healths, items):
    answer = []
    
    for idx,item in enumerate(items):
        else_h = 0
        for h in healths:
            if else_h < h-item[1]:
                else_h = h-item[1]
    
        if else_h >= 100:
            answer.append(idx+1)
    
    return answer
