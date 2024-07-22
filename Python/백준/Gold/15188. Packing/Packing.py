def solve(n, w1, w2):
    presents = [False] * n
    total = 0
    for w in [w1, w2]:
        dp = [[0] * (w + 1) for _ in range(n + 1)]
        visited = [[[] for _ in range(w + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, w + 1):
                if j < weight[i - 1] or presents[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                    visited[i][j] = visited[i - 1][j][:]
                else:
                    if dp[i - 1][j] < dp[i - 1][j - weight[i - 1]] + value[i - 1]:
                        dp[i][j] = dp[i - 1][j - weight[i - 1]] + value[i - 1]
                        visited[i][j] = visited[i - 1][j - weight[i - 1]][:] + [i - 1]
                    else:
                        dp[i][j] = dp[i - 1][j]
                        visited[i][j] = visited[i - 1][j][:]
        
        for v in visited[n][w]:
            presents[v] = True
        total += dp[n][w]
    return total

P = int(input())

for p in range(P):
    N, W1, W2 = map(int, input().split())
    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))

    print('Problem ' + str(p + 1) + ': ' + str(max(solve(N, W1, W2), solve(N, W2, W1))))
