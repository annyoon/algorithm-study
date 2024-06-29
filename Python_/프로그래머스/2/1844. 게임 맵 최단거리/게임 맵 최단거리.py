from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 오 아래 왼 위

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    
    dist[0][0] = 1
    q.append([[0, 0], 1])
    result = bfs(maps, dist, q, n, m)
    
    return result

def bfs(maps, dist, q, n, m):
    global dx, dy
    while len(q) > 0:
        cur = q.popleft()
        
        if cur[0] == [n - 1, m - 1]:
            return cur[1]
        
        for i in range(4):
            n_cur = [cur[0][0] + dx[i], cur[0][1] + dy[i]]
            if inRange(n_cur[0], n_cur[1], n, m):
                if maps[n_cur[0]][n_cur[1]] == 1 and dist[n_cur[0]][n_cur[1]] == -1:
                    dist[n_cur[0]][n_cur[1]] = cur[1] + 1
                    q.append([n_cur, cur[1] + 1])
                
    return -1

def inRange(row, col, n, m):
    return 0 <= row < n and 0 <= col < m