from collections import deque

N, M = 0, 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
lever = [0, 0]

def solution(maps):
    global N, M
    N, M = len(maps), len(maps[0])
    q = deque()
    dist = [[-1] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                q.append([i, j])
                dist[i][j] = 0
                
    result = bfs(q, maps, dist, 'L')
    if result == -1:
        return result
    
    q = deque()
    q.append(lever)
    dist = [[-1] * M for _ in range(N)]
    dist[lever[0]][lever[1]] = 0
    
    tmp = bfs(q, maps, dist, 'E')
    if tmp == -1:
        return tmp
    else:
        return result + tmp

def bfs(q, maps, dist, dst):
    while q:
        global lever
        cur = q.popleft()

        if maps[cur[0]][cur[1]] == dst:
            lever = cur
            return dist[cur[0]][cur[1]]

        for i in range(4):
            nCur = [cur[0] + dx[i], cur[1] + dy[i]]
            if inRange(nCur) and maps[nCur[0]][nCur[1]] != 'X':
                if dist[nCur[0]][nCur[1]] == -1:
                    dist[nCur[0]][nCur[1]] = dist[cur[0]][cur[1]] + 1
                    q.append(nCur)
    return -1
        
def inRange(cur):
    return 0 <= cur[0] < N and 0 <= cur[1] < M
