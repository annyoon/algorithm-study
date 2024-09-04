N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))
dist = sorted([abs(arr[i + 1] - arr[i]) for i in range(N - 1)])
answer = 0

for i in range(N - K):
    answer += dist[i]

print(answer)
