import heapq

N, M = map(int, input().split())
barn = [list(map(int, input().split())) for _ in range(M)]
arr = [[] for _ in range(N + 1)]
dist = [1e8] * (N + 1)

for b in barn:
    arr[b[0]].append((b[1], b[2]))
    arr[b[1]].append((b[0], b[2]))

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    dist[start] = 0

    while q:
        cur, weight = heapq.heappop(q)

        if dist[cur] < weight:
            continue

        for a in arr[cur]:
            if dist[a[0]] > weight + a[1]:
                heapq.heappush(q, (a[0], weight + a[1]))
                dist[a[0]] = weight + a[1]

dijkstra(1)
print(dist[N])
