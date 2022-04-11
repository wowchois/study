'''
모든 경우의 count로 재귀함수 사용.

[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
'''

def solution(numbers, target):
    answer = 0
    answer += loop(numbers[0],1,numbers,target,'')
    answer += loop(-numbers[0],1,numbers,target,'')
    
    return answer

def loop(prev,idx,numbers,target,flag):
    if idx == len(numbers) :
        if prev == target :
            return 1
        return 0
    
    result = 0
    result += loop(prev+numbers[idx],idx+1,numbers,target,'+')
    result += loop(prev-numbers[idx],idx+1,numbers,target,'-')

    return result
