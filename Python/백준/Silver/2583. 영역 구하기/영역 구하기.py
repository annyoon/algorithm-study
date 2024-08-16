import sys
sys.setrecursionlimit(10 ** 5)

def dfs(cur):
    global depth
    visited[cur[0]][cur[1]] = True
    depth += 1
    
    for d in range(4):
        nCur = [cur[0] + dx[d], cur[1] + dy[d]]
        if inRange(nCur) and not board[nCur[0]][nCur[1]] and not visited[nCur[0]][nCur[1]]:
            dfs(nCur)

def inRange(cur):
    return 0 <= cur[0] < m and 0 <= cur[1] < n

m, n, k = list(map(int, input().split()))
board = [[False] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
count, depth = 0, 0
result = []

for _ in range(k):
    arr = list(map(int, input().split()))
    for i in range(m - arr[3], m - arr[1]):
        for j in range(arr[0], arr[2]):
            board[i][j] = True

for i in range(m):
    for j in range(n):
        if not board[i][j] and not visited[i][j]:
            depth = 0
            count += 1
            dfs([i, j])
            result.append(depth)

print(count)
for r in sorted(result):
    print(r, end = ' ')
