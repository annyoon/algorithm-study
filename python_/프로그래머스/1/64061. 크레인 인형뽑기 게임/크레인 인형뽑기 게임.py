def solution(board, moves):
    answer = 0
    arr= []
    
    for m in moves:
        m -= 1
        
        for i in range(len(board)):
            if board[i][m] != 0:
                if len(arr) != 0:
                    if arr[len(arr) - 1] == board[i][m]:
                        arr.pop()
                        answer += 1
                    else:
                        arr.append(board[i][m])
                else:
                    arr.append(board[i][m])
                board[i][m] = 0
                break
                
    return answer * 2
