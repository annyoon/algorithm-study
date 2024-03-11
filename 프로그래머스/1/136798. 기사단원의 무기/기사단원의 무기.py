def solution(number, limit, power):
    answer = 0

    for n in range(1, number + 1):
        num = solve(n)
        if num > limit:
            answer += power
        else:
            answer += num

    return answer

def solve(n):
    num = 0

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            num += 1
            if i * i != n:
                num += 1

    return num
