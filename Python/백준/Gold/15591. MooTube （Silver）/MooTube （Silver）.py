from collections import deque

N, Q = map(int, input().split())
graph, visited = [[] for _ in range(N + 1)], []
q = deque()

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

def bfs(k):
    answer = 0
    while q:
        cur, u = q.pop()
        for ncur, nu in graph[cur]:
            nu = min(nu, u)
            if not visited[ncur] and nu >= k:
                answer += 1
                visited[ncur] = True
                q.append((ncur, nu))
    return answer

for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N + 1)
    visited[v] = True
    q = deque([(v, float('inf'))])
    print(bfs(k))
