def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer = answer + i if calculate(i) % 2 == 0 else answer - i
    return answer

def calculate(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += 1
    return result