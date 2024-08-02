def solution(board):
    existWinner, winner = False, ''
    countO, countX = 0, 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                countO += 1
            elif board[i][j] == 'X':
                countX += 1
            else:
                continue
            
            count = check(i, j, board)
            if existWinner and count > 0 and winner != board[i][j]:
                return 0
            if count > 0:
                existWinner = True
                winner = board[i][j]
                
    if countO < countX:
        return 0
    if countO - countX > 1:
        return 0
    if existWinner:
        if winner == 'O' and countO - countX != 1:
            return 0
        if winner == 'X' and countO != countX:
            return 0
        
    return 1

def check(r, c, board):
    count = 0
    arr = [
        [[1, 2], [0, 0]],
        [[0, 0], [1, 2]],
        [[1, 2], [1, 2]],
        [[-1, -2], [1, 2]]
    ]
    for a in arr:
        for i in range(2):
            nr, nc = r + a[0][i], c + a[1][i]
            if not inRange(nr, nc) or board[r][c] != board[nr][nc]:
                break
            if i == 1:
                count += 1
    return count

def inRange(r, c):
    return 0 <= r < 3 and 0 <= c < 3
