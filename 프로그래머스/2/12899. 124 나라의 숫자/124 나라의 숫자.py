def solution(n):
    arr = ['1', '2', '4']
    result = ''
    while n > 0:
        n -= 1
        result = arr[n % 3] + result
        n //= 3
    return result
