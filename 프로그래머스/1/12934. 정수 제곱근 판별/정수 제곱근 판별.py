def solution(n):
    answer = 0
    num = n ** (1 / 2)
    return (num + 1) ** 2 if num % 1 == 0 else -1