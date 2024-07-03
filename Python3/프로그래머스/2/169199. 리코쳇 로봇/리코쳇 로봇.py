from collections import deque

n, m = 0, 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def solution(board):
    global n, m
    n = len(board)
    m = len(board[0])
    
    q = deque()
    dist = [[-1] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append([i, j])
                dist[i][j] = 0
                return bfs(board, dist, q) 

def bfs(board, dist, q):
    while q:
        cur = q.popleft()
        
        if board[cur[0]][cur[1]] == 'G':
            return dist[cur[0]][cur[1]]
        
        for i in range(4):
            s = 1
            nCur = [cur[0] + dx[i] * s, cur[1] + dy[i] * s]
            while inRange(nCur) and board[nCur[0]][nCur[1]] != 'D':
                s += 1
                nCur = [cur[0] + dx[i] * s, cur[1] + dy[i] * s]
            nCur = [cur[0] + dx[i] * (s - 1), cur[1] + dy[i] * (s - 1)]
            if dist[nCur[0]][nCur[1]] == -1:
                dist[nCur[0]][nCur[1]] = dist[cur[0]][cur[1]] + 1
                q.append(nCur)
    return -1
            
def inRange(cur):
    return 0 <= cur[0] < n and 0 <= cur[1] < m
