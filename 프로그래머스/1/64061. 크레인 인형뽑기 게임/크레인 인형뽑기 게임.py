def solution(board, moves):
    arr= []
    result = 0
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                if len(arr):
                    if arr[len(arr) - 1] == board[i][m - 1]:
                        arr.pop()
                        result += 1
                    else:
                        arr.append(board[i][m - 1])
                else:
                    arr.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
                
    return result * 2