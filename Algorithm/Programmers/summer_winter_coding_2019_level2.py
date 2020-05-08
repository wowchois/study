#Summer/Winter Coding(2019)
#level 2 - 멀쩡한 사각형
#풀이 : w,h의 최대공약수 구해서 풀기

import math

def solution(w,h):
    answer = 1
    
    gcd = math.gcd(w,h)
    delete = (w//gcd) + (h//gcd) - 1
    answer = (w * h) - (gcd * delete)
    
    return answer