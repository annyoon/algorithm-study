import sys
sys.setrecursionlimit(10 ** 9)

def dfs(cur):
    global population
    
    country.append(cur)
    population += board[cur[0]][cur[1]]
    visited[cur[0]][cur[1]] = True

    for d in range(4):
        nCur = [cur[0] + dx[d], cur[1] + dy[d]]
        if inRange(nCur) and not visited[nCur[0]][nCur[1]]:
            if L <= abs(board[cur[0]][cur[1]] - board[nCur[0]][nCur[1]]) <= R:
                dfs(nCur)

def inRange(cur):
    return 0 <= cur[0] < N and 0 <= cur[1] < N

def move(arr):
    newPopulation = population // len(arr)
    for a in arr:
        board[a[0]][a[1]] = newPopulation

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
country, population = [], 0
result = 0

while True:
    didMove = False
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            country, population = [], 0
            if not visited[i][j]:
                dfs([i, j])
            if len(country) > 1:
                move(country)
                didMove = True

    if didMove:
        result += 1
    else:
        break

print(result)
