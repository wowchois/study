
'''
정렬 유형

TEST CASE

numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
[0, 0, 0] "0"
'''


def solution(numbers):
    answer = ''
    if sum(numbers) == 0: return '0'
    
    n_arr = list(map(str,numbers))
    n_arr.sort(key=lambda n: n*3,reverse=True) 

    return ''.join(n_arr)
