def solution(n, m):
    answer = []
    numMin = min(n, m)
    numMax = max(n, m)
    for num in range(numMin, -1, -1):
        if n % num == 0 and m % num == 0:
            answer.append(num)
            break
    for num in range(1, numMin + 1):
        if (numMax * num) % numMin == 0:
            answer.append(numMax * num)
            break
    return answer