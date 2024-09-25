R, C, N = map(int, input().split())
board = [list(input()) for _ in range(R)]

def setBomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'

def bomb():
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'X':
                board[i][j] = '.'
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if inRange(ni, nj) and board[ni][nj] != 'X':
                        board[ni][nj] = '.'

def inRange(i, j):
    return 0 <= i < R and 0 <= j < C

for t in range(2, N + 1):
    if t % 2 == 0:
        setBomb()
    else:
        bomb()
    
for i in range(R):
    for j in range(C):
        if board[i][j] == 'X':
            print('O', end = '')
        else:
            print(board[i][j], end = '')
    print()
