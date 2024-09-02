from itertools import combinations_with_replacement

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

dic = {}
result = 0

combinations = list(combinations_with_replacement(arr, r = 2))

for x, y in combinations:
    if x + y not in dic:
        dic[x + y] = True

for z, k in combinations:
    if k - z in dic:
        result = max(k, result)

print(result)
