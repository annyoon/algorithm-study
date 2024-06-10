from collections import deque

def solution(x, y, n):
    def check(n_cur):
        return n_cur <= y and dist[n_cur] == -1
    
    q = deque()
    q.append(x)
    
    dist = {}
    for i in range(x, y + 1):
        dist[i] = -1
    dist[x] = 0
    
    while q:
        cur = q.popleft()
        if cur == y:
            return dist[cur]
        
        for i in range(3):
            if i == 0 and check(cur + n):
                q.append(cur + n)
                dist[cur + n] = dist[cur] + 1
            elif i == 1 and check(cur * 2):
                q.append(cur * 2)
                dist[cur * 2] = dist[cur] + 1
            elif i == 2 and check(cur * 3):
                q.append(cur * 3)
                dist[cur * 3] = dist[cur] + 1
                
    return -1
    