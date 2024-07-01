def solution(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 2
    
    for w in range(3, n + 1):
        arr[w] = (arr[w - 1] + arr[w - 2]) % (10 ** 9 + 7)
        
    return arr[n]
