N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
answer = 0

def dfs(cur, depth, sumNumbers):
    global visited, answer

    if depth == 3:
        answer = max(answer, sumNumbers)
        return
    for d in range(4):
        nCur = [cur[0] + dx[d], cur[1] + dy[d]]
        if inRange(nCur) and not visited[nCur[0]][nCur[1]]:
            visited[nCur[0]][nCur[1]] = True
            dfs(nCur, depth + 1, sumNumbers + board[nCur[0]][nCur[1]])
            visited[nCur[0]][nCur[1]] = False

def check(cur):
    global answer

    for d in range(4):
        sumNumbers = board[cur[0]][cur[1]]
        nCur = [cur[0] + dx[d], cur[1] + dy[d]]
        if not inRange(nCur):
            continue
        sumNumbers += board[nCur[0]][nCur[1]]
        if d == 0 or d == 2:
            if M <= nCur[1] + 1 or nCur[1] - 1 < 0:
                continue
            sumNumbers += board[nCur[0]][nCur[1] + 1] + board[nCur[0]][nCur[1] - 1]
        else:
            if N <= nCur[0] + 1 or nCur[0] - 1 < 0:
                continue
            sumNumbers += board[nCur[0] + 1][nCur[1]] + board[nCur[0] - 1][nCur[1]]
        answer = max(answer, sumNumbers)

def inRange(cur):
    return 0 <= cur[0] < N and 0 <= cur[1] < M

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs([i, j], 0, board[i][j])
        visited[i][j] = False
        check([i, j])

print(answer)
