def solution(board, h, w):
    def inRange(h, w):
        return 0 <= h < n and 0 <= w < n
    
    n = len(board)
    count = 0
    dh, dw = [1, 0, -1, 0], [0, 1, 0, -1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        if inRange(h_check, w_check):
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count
