def solution(arr, divisor):
    answer = []
    for n in sorted(arr):
        if n % divisor == 0:
            answer.append(n)
    return answer if len(answer) > 0 else [-1]