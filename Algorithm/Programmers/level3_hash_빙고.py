'''
Hash 유형

TEST CASE

[[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]	[14,3,2,4,13,1,16,11,5,15]	3
[[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]]	[15,7,2,25,9,16,12,18,5,4,10,13,20]	2
'''

'''
1. 그냥 while+2중포문 / 3중포문으로 접근하기에는 효율성이 없다. -> nums를 hash로 변환해서 직접 접근 O(1)
2. nums에 해당하는 숫자 모두 0으로 변경한 후 몇개 빙고인지 센다.
3. 가로/세로/대각선/-대각선 4가지 케이스가 있어서 각각 케이스별로 더한 후 총 값이 0이면 answer에 추가.
'''
def solution(board, nums):
    answer = 0
    length = len(board)
    n_dict = {n : 0 for n in nums}
    
    for i in range(length):
        for j in range(length):
            try:
                board[i][j] = n_dict[board[i][j]]
            except:
                continue
        
    cross_sum = 0   # \ (index 0부터 시작하는 대각선)
    m_cross_sum = 0 # / (index 뒤에서부터 시작하는 대각선)
    
    for i in range(length):
        col_sum = 0
        for j in range(length):
            col_sum += board[j][i]
        cross_sum += board[i][i]
        m_cross_sum += board[i][length-i-1]
        
        if sum(board[i]) == 0: answer += 1  #행
        if col_sum == 0: answer += 1        #열
    if cross_sum == 0: answer += 1
    if m_cross_sum == 0: answer += 1    
    
    return answer

