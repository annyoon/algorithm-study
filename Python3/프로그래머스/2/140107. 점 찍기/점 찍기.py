def solution(k, d):
    count = 0
    for x in range(d + 1):
        if x % k == 0:
            y = (d ** 2 - x ** 2) ** (1 / 2)
            count += y // k + 1
    return count
