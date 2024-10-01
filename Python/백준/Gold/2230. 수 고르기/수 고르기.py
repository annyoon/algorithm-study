N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

def solve():
    answer = 2e9
    left, right = 0, 0

    while left <= right and right < N:
        if numbers[right] - numbers[left] == M:
            return M
        if numbers[right] - numbers[left] > M:
            answer = min(answer, numbers[right] - numbers[left])
            left += 1
        else:
            right += 1

    return answer

print(solve())
