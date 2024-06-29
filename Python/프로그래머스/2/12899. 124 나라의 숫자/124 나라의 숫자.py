def solution(n):
    arr = ['1', '2', '4']
    result = ''
    while n > 0:
        result = arr[(n - 1) % 3] + result
        n = (n - 1) // 3
    return result
