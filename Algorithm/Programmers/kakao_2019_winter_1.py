#2019 카카오 개발자 겨울 인턴십
#Level 1 - 크레인 인형뽑기 게임

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    basket = []
    
    for j in range(len(moves)) :
        m = moves[j] - 1
        for i in range(len(board)) :
            if board[i][m] != 0 : #값 있을 때
                if len(basket) == 0 :
                    basket.append(board[i][m])
                    board[i][m] = 0
                    break
                if board[i][m] == basket[len(basket)-1] :
                    answer += 2
                    basket.pop()
                    board[i][m] = 0
                else :
                    basket.append(board[i][m])
                    board[i][m] = 0
                break
    
    return answer

solution(board, moves)