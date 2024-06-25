import sys
sys.setrecursionlimit(10 ** 6)
count = 0

def solution(maps):
    global count
    result = []
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    def inRange(cur):
        return 0 <= cur[0] < n and 0 <= cur[1] < m
            
    def dfs(cur):
        global count
        count += int(maps[cur[0]][cur[1]])
        visited[cur[0]][cur[1]] = True
        
        for i in range(4):
            n_cur = [cur[0] + dx[i], cur[1] + dy[i]]
            if inRange(n_cur) and maps[n_cur[0]][n_cur[1]] != 'X':
                if not visited[n_cur[0]][n_cur[1]]:
                    dfs(n_cur)
                    
    for r in range(n):
        for c in range(m):
            if maps[r][c] != 'X' and not visited[r][c]:
                dfs([r, c])
                if count != 0:
                    result.append(count)
                    count = 0
                
    return sorted(result) if len(result) > 0 else [-1]
