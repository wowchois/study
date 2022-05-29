'''
동적계획법 유형

TEST CASE

N	number	return
5	12	4
2	11	3

'''


#총 n개만큼 순회 (n=number인경우 1개라서 리턴)
#사칙연산과 n개수만큼합쳐진 문자열의 집합을 만든다.
#집합을 리스트에 담고 다음 집합과 새로운 사칙연산+문자열 집합을 만든다.
#number가 계산값집합에 포함된 경우 리턴
    
def solution(N, number):
    if N == number: return 1

    set_list = []
    for i in range(1,9):
        group_list = {int(i * str(N))}
        
        for j in range(len(set_list)):
            first = set_list[j]
            last = set_list[-j-1]
            
            for f in first:
                for l in last:
                    group_list.add(f+l)
                    group_list.add(f-l)
                    group_list.add(l-f)
                    group_list.add(f*l)
                    if l != 0:
                        group_list.add(f//l)
                    if f != 0:
                        group_list.add(l//f)
        
        if number in group_list:
            return i
        set_list.append(group_list)
    
    return -1
