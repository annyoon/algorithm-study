def solution(a, b):
    answer = 0
    start = a
    end = b
    if a > b:
        start = b
        end = a
    for i in range(start, end + 1):
        answer += i
    return answer