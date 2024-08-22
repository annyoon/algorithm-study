n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]

board = [[False] * (n + 1) for _ in range(n + 1)]
for a in arr:
    board[a[0]][a[1]] = True
    board[a[1]][a[0]] = True

visited = [False] * (n + 1)


def dfs(cur):
    global result

    if visited[cur]:
        return
    visited[cur] = True
    result += 1

    for i in range(1, n + 1):
        if board[cur][i]:
            dfs(i)


result = -1
dfs(1)
print(result)
