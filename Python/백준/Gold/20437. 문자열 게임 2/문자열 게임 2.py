# 답 참고

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    v = list(map(lambda x: ord(x) - 97, input().strip()))
    k, mn, mx = int(input()), len(v), -1

    pos = [[] for _ in range(26)]
    for idx, val in enumerate(v):
        pos[val].append(idx)

    for p in pos:
        for i in range(len(p) - k + 1):
            mn = min(mn, p[i + k - 1] - p[i] + 1)
            mx = max(mx, p[i + k - 1] - p[i] + 1)

    print(-1 if mx == -1 else f"{mn} {mx}")
