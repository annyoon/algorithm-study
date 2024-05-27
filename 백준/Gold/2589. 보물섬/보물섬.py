from collections import deque

r, c = map(int, input().split())
board = [input() for _ in range(r)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
answer = 0


def bfs(q, dist, maxNum):
    while q:
        cur = q.popleft()
        maxNum = max(maxNum, dist[cur[0]][cur[1]])
        for i in range(4):
            nCur = [cur[0] + dx[i], cur[1] + dy[i]]
            if inRange(nCur) and board[nCur[0]][nCur[1]] == "L":
                if dist[nCur[0]][nCur[1]] == -1:
                    dist[nCur[0]][nCur[1]] = dist[cur[0]][cur[1]] + 1
                    q.append(nCur)
    return maxNum


def inRange(cur):
    return 0 <= cur[0] < r and 0 <= cur[1] < c


for i in range(r):
    for j in range(c):
        if board[i][j] == "L":
            q = deque()
            dist = [[-1] * c for _ in range(r)]
            q.append([i, j])
            dist[i][j] = 0
            answer = bfs(q, dist, answer)

print(answer)
