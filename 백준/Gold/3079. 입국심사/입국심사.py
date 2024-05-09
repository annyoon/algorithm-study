n, m = map(int, input().split())
cost = [int(input()) for _ in range(n)]
left = min(cost)
right = 10 ** 18
result = right

while left <= right:
    mid = (left + right) // 2

    temp = 0
    for c in cost:
        temp += mid // c

    if temp >= m:
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1

print(result)
