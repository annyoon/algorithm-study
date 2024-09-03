N = int(input())
arr = list(map(int, input().split()))
stack = [0]
result = [-1] * N

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)
