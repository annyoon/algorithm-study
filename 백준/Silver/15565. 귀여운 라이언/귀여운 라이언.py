from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
result = []
count = 1 if arr[left] == 1 else 0

while left < len(arr) and right < len(arr):
    if count < K:
        right += 1
        if right < len(arr) and arr[right] == 1:
            count += 1
    elif count == K:
        result.append(right - left + 1)
        if left < len(arr) and arr[left] == 1:
            count -= 1
        left += 1

print(min(result) if len(result) else -1)
